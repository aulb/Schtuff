# https://hexdocs.pm/elixir/IO.html
# http://elixir-lang.org/docs/stable/elixir/File.html
defmodule CowInterrogator do
	def get_name do
		IO.gets("whats yo name? ") |> String.trim # probably same as python trim
	end

	def get_cow_lover do
		IO.getn("Do you like cows? [y|n] ", 1) # read the docs....
	end

	def interrogate do
		name = get_name
		case String.downcase(get_cow_lover) do
			"y" ->
				IO.puts "great! heres a cow for ya #{name}"
				IO.puts "placeholder" # cow_art
			"n" ->
				IO.puts "same as y"
			_ -> 
				IO.puts "not y or n, default statement"
		end
	end

	def cow_art do
		
	end
end

CowInterrogator.interrogate # execute
