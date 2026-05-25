import { Router } from "express";
import { Dex } from "@pkmn/sim";
import { createBattle, makeChoice } from "./battle";

const router = Router();

router.get("/health", (req, res) => {
    res.json({ status: "ok" });
});

router.post("/battle/create", (req, res) => {
    console.log(req.body);
    const { options, p1, p2 } = req.body;
    // const battleId = randomUUID();
    // createBattle(battleId, options, p1, p2);

    // HERE IS HOW TO TEST:
    // npx tsx src/index
    //curl -X POST http://localhost:3000/api/battle/create -H "Content-Type: application/json" -d "{\"options\":{\"formatid\":\"gen1customgame\"},\"p1\":{\"name\":\"Ash\",\"team\":[]},\"p2\":{\"name\":\"Gary\",\"team\":[]}}"
    res.json({ "333": "ok" });
});

// router.post("/battle/:id/move", (req, res) => {
//     const { p1Choice, p2Choice } = req.body;
//     const result = makeChoice(req.params.id, p1Choice, p2Choice);
//     res.json(result);
// });

router.get("/pokedex/:name", (req, res) => {
    const data = Dex.species.get(req.params.name);
    if (!data.exists) return res.status(404).json({ error: "Not found" });
    res.json(data);
});

router.get("/learnset/:name", async (req, res) => {
    const learnset = await Dex.learnsets.get(req.params.name);
    if (!learnset) return res.status(404).json({ error: "Not found" });
    res.json(learnset.learnset);
});

export default router;
