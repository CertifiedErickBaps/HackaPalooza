const express = require("express");

const app = express();

const path = require("path");

// habilitar carpeta public
app.use(express.static(path.resolve(__dirname, "../public")));

app.listen(8080, () => {
  console.log("Escuchando puerto: ", 8080);
});


