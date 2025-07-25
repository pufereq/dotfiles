-- disable telemetry for copilot
return {
  "zbirenbaum/copilot.lua",
  lazy = false,
  priority = 1000,
  build = ":Copilot auth",
  opts = {
    panel = { enabled = false },
    suggestion = {
      enabled = true,
      auto_trigger = true,
      hide_during_completion = true,
      debounce = 75,
    },
    server_opts_overrides = {
      settings = {
        telemetry = {
          telemetryLevel = "off",
        },
      },
    },
  },
}
