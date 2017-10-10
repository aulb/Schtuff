# Start with the tests, like what are we expecting..., then build the damn thing
defmodule TimeConversion do
	def main(input) do
		# pipe input to converter and return it
		input |> converter
	end

	def converter(input) do
		[hours, minutes, seconds] = String.split(input, ":")
		# Slice string from index 2 - 3 inclusive '00AM'[2..3] -> AM
		period = String.slice(seconds, 2..3)
		seconds = String.slice(seconds, 0..1)
		formated_hour = format_hour(period, hours)

		# Return...
		"#{formated_hour}:#{minutes}:#{seconds}"
	end

	# defp: tldr private
	# https://stackoverflow.com/questions/35735762/whats-the-difference-between-def-and-defp-in-the-phoenix-framework
	# hardcode
	defp format_hour("AM", "12"), do: "00"
	defp format_hour("AM", hours), do: hours
	defp format_hour("PM", "12"), do: "12"
	defp format_hour("PM", hours), do: "#{String.to_integer(hours) + 12}"
end

input = IO.gets("") |> String.trim
TimeConversion.main(input) |> IO.puts
