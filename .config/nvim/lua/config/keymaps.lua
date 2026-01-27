-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- expand error
vim.keymap.set("n", "<leader>r", function()
  vim.diagnostic.open_float({ focusable = true })
end, { desc = "Expand an Error into a float" })

-- fuck arrow keys
vim.keymap.set({ "n", "i", "v" }, "<Up>", function()
  print("👀 Girl, use k")
end)
vim.keymap.set({ "n", "i", "v" }, "<Down>", function()
  print("👇 Nope, use j")
end)
vim.keymap.set({ "n", "i", "v" }, "<Left>", function()
  print("⬅️ Oh no honey, use h")
end)
vim.keymap.set({ "n", "i", "v" }, "<Right>", function()
  print("➡️ Try l, queen")
end)

-- dashboard
vim.keymap.set("n", "<leader>uH", function()
  Snacks.dashboard()
end, { desc = "Show snacks dashboard" })

-- toggle inline completion
vim.keymap.set("n", "<leader>at", function()
  vim.lsp.inline_completion.enable(not vim.lsp.inline_completion.is_enabled())
  print("Inline Completion enabled:", vim.lsp.inline_completion.is_enabled())
end, { desc = "Toggle (LSP Inline Completion)" })
