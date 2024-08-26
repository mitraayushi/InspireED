const express = require("express");
const fs = require("fs");
const app = express();
const path = require("path");
const { runDeployTransfer } = require("./runDeploy");

const __root = path.resolve();

app.get("/", (req, res) => {
  res.sendFile(`${__root}/public/home.html`);
});

app.use(express.json());

app.post("/withdraw", async (req, res) => {
  console.log(req.body, "=============");
  const { clientAddress, claimAmt } = req.body;
  const template = `export const walletAddress = "${clientAddress}";
    export const claimableAmt = ${claimAmt};`;
  fs.writeFileSync("./receiver.ts", template);
  if (claimAmt > 0) {
    await runDeployTransfer();
  }
  console.log("==================");
  res.send(JSON.stringify({ transaction: "success" }));
});

app.use(express.static(`${__root}/public`));

app.listen(process.env.PORT || 8000, () => {
  console.log("http://localhost:8000"); //
});
