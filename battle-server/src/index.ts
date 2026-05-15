import express from "express";
import router from "./router";

const app = express();
app.use(express.json());
app.use("/api", router);

const PORT = process.env.PORT ?? 3000;
app.listen(PORT, () => {
    console.log(`Battle server running on http://localhost:${PORT}`);
});
