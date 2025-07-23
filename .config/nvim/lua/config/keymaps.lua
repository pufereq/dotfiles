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

local api = vim.api
local opts = { noremap = true, silent = true }

local amongus_schlong = {
  "⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
  "⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
  "⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
  "⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
  "⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀",
  "⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆",
  "⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟",
  "⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀",
  "⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀",
  "⠀⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀",
  "⠀⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀",
  "⠀⠀⠀⠀⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀",
  "⠀⠀⠀⠀⠀⠙⠛⠛⠛⠋⠁⠀⠙⠻⠿⠟⠋⠑⠛⠋⠀",
}

local function show_amogus()
  local buf = api.nvim_create_buf(false, true)
  api.nvim_buf_set_lines(buf, 0, -1, false, amongus_schlong)

  local win = api.nvim_open_win(buf, false, {
    relative = "editor",
    width = 32,
    height = #amongus_schlong,
    row = math.floor((vim.o.lines - #amongus_schlong + 2) / 2),
    col = math.floor((vim.o.columns - 30) / 2),
    style = "minimal",
    border = "shadow",
  })

  vim.defer_fn(function()
    if api.nvim_win_is_valid(win) then
      api.nvim_win_close(win, true)
      api.nvim_buf_delete(buf, { force = true })
    end
  end, 1200) -- give it time to emotionally scar you
end

-- map all arrow keys to this madness
for _, key in ipairs({ "<Up>", "<Down>", "<Left>", "<Right>" }) do
  vim.keymap.set({ "n", "i", "v" }, key, function()
    show_amogus()
    vim.cmd("echohl ErrorMsg | echo '🚨 ARROW KEY?! SUS. USE HJKL DUMBASS.' | echohl None")
  end, opts)
end
