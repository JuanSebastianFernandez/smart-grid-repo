function pushTelemetry(payload) {
  return Promise.resolve({ accepted: true, payload });
}

module.exports = { pushTelemetry };

