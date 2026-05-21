import { Battle } from "@pkmn/sim";
import { LogFormatter } from "@pkmn/view";
import { Protocol } from "@pkmn/protocol";
import { Battle as BattleClient, Side } from "@pkmn/client";
import { Generations } from "@pkmn/data";
import { Dex } from "@pkmn/sim";

const gens = new Generations(Dex as any);
const battles: Record<string, any> = {};

function getAvailableMoves(side: any): {
    moves: string[];
    canSwitch: string[];
} {
    const request = side.activeRequest;

    if (!request || request.wait) return { moves: [], canSwitch: [] };

    if (request.forceSwitch) {
        const canSwitch: string[] = [];
        for (let i = 0; i < request.side.pokemon.length; i++) {
            const p = request.side.pokemon[i];
            if (!p.active && !p.condition.endsWith(" fnt")) {
                canSwitch.push(`switch ${i + 1}`);
            }
        }
        return { moves: [], canSwitch };
    }

    const moves: string[] = [];
    for (let i = 0; i < request.active[0].moves.length; i++) {
        if (!request.active[0].moves[i].disabled) {
            moves.push(`move ${i + 1}`);
        }
    }

    const canSwitch: string[] = [];
    for (let i = 0; i < request.side.pokemon.length; i++) {
        const p = request.side.pokemon[i];
        if (!p.active && !p.condition.endsWith(" fnt")) {
            canSwitch.push(`switch ${i + 1}`);
        }
    }

    return { moves, canSwitch };
}

function pickRandomChoice(side: any): string {
    const { moves, canSwitch } = getAvailableMoves(side);
    console.log(moves, canSwitch);
    const options = moves.length > 0 ? moves : canSwitch;
    return options[Math.floor(Math.random() * options.length)];
}

function getLog(battle: any, formatter: any, client: any, fromIndex = 0) {
    let completeLog: string[] = [];
    let skipNext = false;
    for (const line of battle.log.slice(fromIndex)) {
        if (line.startsWith(`|split|`)) {
            skipNext = true;
            continue;
        }
        if (skipNext) {
            skipNext = false;
            continue;
        }
        for (const { args, kwArgs } of Protocol.parse(line)) {
            let text = (formatter as any).formatText(args, kwArgs);
            client.add(args, kwArgs);
            text = text.trim();
            if (!text) continue;
            text = text
                .replace(/\|\|[^|]+\|\|/g, "")
                .replace(/\|\|/g, "")
                .trim();
            completeLog.push(text);
        }
    }
    return completeLog.join("\n");
}

export function createBattle(
    battleId: string,
    options: any,
    p1Data: any,
    p2Data: any
) {
    const battle = new Battle(options);
    const p1client = new BattleClient(gens, "p1");
    const p2client = new BattleClient(gens, "p2");
    const p1formatter = new LogFormatter("p1", p1client);
    const p2formatter = new LogFormatter("p2", p2client);

    battle.setPlayer("p1", p1Data);
    battle.setPlayer("p2", p2Data);

    for (const line of battle.log) {
        for (const { args, kwArgs } of Protocol.parse(line)) {
            p1client.add(args, kwArgs);
            p2client.add(args, kwArgs);
        }
    }

    battles[battleId] = {
        battle,
        p1client,
        p2client,
        p1formatter,
        p2formatter,
        lastLogIndex: battle.log.length,
    };
}

export function makeChoice(
    battleId: string,
    p1Choice: string,
    p2Choice: string
) {
    const session = battles[battleId];
    if (!session) throw new Error("Battle not found: " + battleId);
    const logIndexBefore = session.lastLogIndex;

    if (p1Choice) session.battle.choose("p1", p1Choice);
    if (p2Choice) session.battle.choose("p2", p2Choice);

    const p1Log = getLog(
        session.battle,
        session.p1formatter,
        session.p1client,
        logIndexBefore
    );
    const p2Log = getLog(
        session.battle,
        session.p2formatter,
        session.p2client,
        logIndexBefore
    );

    session.lastLogIndex = session.battle.log.length;

    return {
        p1Log,
        p2Log,
        ended: session.battle.ended,
        winner: session.battle.winner,
    };
}

// ─── Simulation ──────────────────────────────────────────────────────────────

function simulate() {
    const battleId = "test-battle";

    const p1Team = [
        {
            name: "Pikachu",
            species: "Pikachu",
            item: "lightball",
            ability: "static",
            moves: ["thunderbolt", "quickattack", "irontail", "thunder"],
            evs: { hp: 4, spa: 252, spe: 252 },
            nature: "Timid",
        },
        {
            name: "Bulbasaur",
            species: "Bulbasaur",
            item: "miracleseed",
            ability: "overgrow",
            moves: ["razorleaf", "sleeppowder", "leechseed", "sludgebomb"],
            evs: { hp: 252, spa: 252, spe: 4 },
            nature: "Modest",
        },
        {
            name: "Squirtle",
            species: "Squirtle",
            item: "mysticwater",
            ability: "torrent",
            moves: ["watergun", "icebeam", "rapidspin", "protect"],
            evs: { hp: 252, def: 252, spd: 4 },
            nature: "Bold",
        },
    ];

    const p2Team = [
        {
            name: "Charmander",
            species: "Charmander",
            item: "charcoal",
            ability: "blaze",
            moves: ["ember", "scratch", "smokescreen", "flamethrower"],
            evs: { hp: 4, spa: 252, spe: 252 },
            nature: "Timid",
        },
        {
            name: "Geodude",
            species: "Geodude",
            item: "hardstone",
            ability: "sturdy",
            moves: ["rockthrow", "magnitude", "defensecurl", "rollout"],
            evs: { hp: 252, atk: 252, def: 4 },
            nature: "Adamant",
        },
        {
            name: "Gastly",
            species: "Gastly",
            item: "spelltag",
            ability: "levitate",
            moves: ["lick", "nightshade", "hypnosis", "confuseray"],
            evs: { hp: 4, spa: 252, spe: 252 },
            nature: "Timid",
        },
    ];

    createBattle(
        battleId,
        { formatid: "gen1customgame" },
        { name: "Ash", team: p1Team },
        { name: "Gary", team: p2Team }
    );

    const session = battles[battleId];
    const battle: any = session.battle;

    let turn = 0;

    while (!battle.ended && turn < 30) {
        turn++;

        const p1Available = getAvailableMoves(battle.sides[0]);
        const p2Available = getAvailableMoves(battle.sides[1]);

        const p1Choice =
            [...p1Available.moves, ...p1Available.canSwitch].length > 0
                ? pickRandomChoice(battle.sides[0])
                : "";
        const p2Choice =
            [...p2Available.moves, ...p2Available.canSwitch].length > 0
                ? pickRandomChoice(battle.sides[1])
                : "";

        const { p1Log } = makeChoice(battleId, p1Choice, p2Choice);

        if (p1Log) console.log(p1Log);
    }
}

simulate();
