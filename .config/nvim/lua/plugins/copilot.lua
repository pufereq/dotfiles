-- disable telemetry for copilot
return {
  "neovim/nvim-lspconfig",
  opts = {
    servers = {
      copilot = {
        -- stylua: ignore
        keys = {
          {
            "<M-]>",
            function() vim.lsp.inline_completion.select({ count = 1 }) end,
            desc = "Next Copilot Suggestion",
            mode = { "i", "n" },
          },
          {
            "<M-[>",
            function() vim.lsp.inline_completion.select({ count = -1 }) end,
            desc = "Prev Copilot Suggestion",
            mode = { "i", "n" },
          },
        },
        settings = {
          telemetry = {
            telemetryLevel = "off",
          },
        },
      },
    },
    setup = {
      copilot = function()
        vim.schedule(function()
          vim.lsp.inline_completion.enable()
        end)
        -- Accept inline suggestions or next edits
        LazyVim.cmp.actions.ai_accept = function()
          return vim.lsp.inline_completion.get()
        end

        if not LazyVim.has_extra("ai.sidekick") then
          vim.lsp.config("copilot", {
            handlers = {
              didChangeStatus = function(err, res, ctx)
                if err then
                  return
                end
                status[ctx.client_id] = res.kind ~= "Normal" and "error" or res.busy and "pending" or "ok"
                if res.status == "Error" then
                  LazyVim.error("Please use `:LspCopilotSignIn` to sign in to Copilot")
                end
              end,
            },
          })
        end
      end,
    },
  },
}
