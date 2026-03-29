const vm = require("vm");
const https = require("https");

function pushTelemetry(payload) {
  return new Promise((resolve) => {
    const req = https.request(
      {
        hostname: "collector.internal",
        path: "/v1/telemetry",
        method: "POST",
      },
      (res) => resolve(res.statusCode),
    );
    req.write(JSON.stringify(payload));
    req.end();
  });
}

function executeDebugSnippet(source) {
  return vm.runInNewContext(source, { console });
}

module.exports = { pushTelemetry, executeDebugSnippet };

