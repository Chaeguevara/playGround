return {
	{
		"nvim-telescope/telescope.nvim",
		tag = "0.1.8",
		dependencies = { "nvim-lua/plenary.nvim" },
		keys = {
			{
				"<C-f>",
				"<cmd>lua require('telescope.builtin').find_files()<CR>",
				{ noremap = true, silent = true },
			},
			{
				"<leader>fg>",
				"<cmd>lua require('telescope.builtin').live_grep()<CR>",
				{ noremap = true, silent = true },
			},
			{
				"<leader>fb>",
				"<cmd>lua require('telescope.builtin').buffers()<CR>",
				{ noremap = true, silent = true },
			},
			{
				"<leader>fh>",
				"<cmd>lua require('telescope.builtin').help_tags()<CR>",
				{ noremap = true, silent = true },
			},
		},
	},
	{
		"nvim-telescope/telescope-ui-select.nvim",
		config = function()
			require("telescope").setup({
				extensions = {
					["ui-select"] = {
						require("telescope.themes").get_dropdown({
							-- even more opts
						}),
					},
				},
			})
			require("telescope").load_extension("ui-select")
		end,
	},
}
