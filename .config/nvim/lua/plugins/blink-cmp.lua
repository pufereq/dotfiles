return {
  -- make emmet more prioritized than copilot
  "saghen/blink.cmp",
  opts = {
    fuzzy = {
      sorts = {
        function(a, b)
          if (a.client_name == nil or b.client_name == nil) or (a.client_name == b.client_name) then
            return
          end
          return b.client_name == "emmet-language-server"
        end,
        -- default sorts
        "score",
        "sort_text",
      },
    },
  },
}
