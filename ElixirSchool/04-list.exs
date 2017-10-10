ExUnit.start

defmodule ListTest do
	use ExUnit.Case

	def sample do
		["WENDYS", "BURGERKING", "MCD"]
	end

	test "sigil" do
		assert sample == ~w(WENDYS BURGERKING MCD)
	end

	test "head" do
		[head | _] = sample # gets WENDYS
		assert head == "WENDYS" # can be any, just pattern matching
	end

	test "last" do
		[_ | tail] = sample
		assert tail == ~w(BURGERKING MCD) # whats this ~w
	end

	# O(n)
	test "last item" do
		assert List.last(sample) == "MCD"
	end

	test "delete item" do
		assert List.delete(sample, "BURGERKING") == ~w(WENDYS MCD)

		# delete first occurrence
		assert List.delete([1,2,2,3], 2) == [1,2,3]
	end

	# foldr(list, acc, function)
	# Folds (reduces) the given list from the right with a function. Requires an accumulator
	# Enum.reduce is an alternative that is encouraged over
	test "List.fold" do
		list = [20, 10, 5, 2.5]
		sum = List.foldr list, 0, &(&1 + &2) # ?? wtf
		# lambda x, y: x + y ? no lambda x, acc: x + acc 
		# sum takes list variable, starting acc 
		assert sum == 37.5
	end

	test "wrap" do
		# 	wrap(list)
		# Wraps the argument in a list
		assert List.wrap(sample) == sample
		assert List.wrap(1) == [1]
		assert List.wrap([]) == []
		assert List.wrap(nil) == []
	end

	# https://niallburkley.com/blog/elixir-filter-map/
	# DEPRECATED
	test "Enum.filter_map" do
		some = Enum.filter_map sample, &(String.first(&1) >= "M"), &(&1 <> " CHASE")
		assert some == ["WENDYS CHASE", "MCD CHASE"]
	end

	# # filter even numbers
	# filter_fn = fn n ->
	#   rem(n, 2) == 0
	# end

	# # double
	# map_fn = fn n ->
	#   n * 2
	# end

	# some_enum = 1..20

	# # filter_map version
	# Enum.filter_map(some_enum, filter_fn, map_fn)

	# # comprehension version
	# for n <- some_enum, filter_fn.(n), do: map_fn.(n)

	test "list comprehension" do
		some = for n <- sample, String.first(n) < "M", do: n <> " Morgan"
		assert some == [] # cause wendys and mcd starts with w and m
	end
end
