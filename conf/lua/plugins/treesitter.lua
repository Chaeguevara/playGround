return {
	"nvim-treesitter/nvim-treesitter",
	build = ":TSUpdate",
	opts = {
		{
			auto_install = true,
			ensure_installed = { "lua", "javascript", "typescript", "python" },
			highlight = { enable = true },
			indent = { enable = true },
		},
	},
}
