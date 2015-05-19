set noswapfile
set nobackup

set autoindent
set smartindent
set noexpandtab
set softtabstop=4
set smarttab
set shiftwidth=4
set tabstop=4

set nowrap
set encoding=utf-8

set number

syntax enable
colorscheme solarized

map <C-e> :Flisttoggle <CR>
nmap <C-t> :tabedit 
nmap <C-w> :bw<CR>
set mouse=a

cd /var/www
