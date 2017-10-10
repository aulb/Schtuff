ExUnit.start

defmodule MapTest do
	def sample do
		%{foo: 'bar', baz: 'quz'}
	end

	test "Map.get" do
		assert Map.get(sample, :foo) == 'bar'
		assert Map.get(sample, :non_existent) == nil
	end

	test "[]" do
		assert sample[:foo] == 'bar'
		assert sample['foo'] == 'bar' # can also work
		assert sample[:non_existent] == nil
	end

	test "." do
		assert sample.foo == 'bar'
		assert_raise KeyError, fn -> 
			sample.non_existent
		end
	end

	test "Map.fetch" do
		{:ok, val} = Map.fetch(sample, :foo) # => {:ok, 'bar'}
		assert val == 'bar'
		:error = Map.fetch(sample, :non_existent)
	end

	test "Update map using pattern matching syntax" do
		# Can only update existing keys this way # why is it foo: now instead of :foo
		assert %{sample | foo: 'bob'} == %{foo: 'bob', baz: 'quz'}
		# Can't add new keys using this method
		assert_raise KeyError, fn ->
			%{sample | far: 'bob'}
		end
	end

	test "Map.values" do
		# No order, as is tradition
		assert Enum.sort(Map.values(sample)) == ['bar', 'quz']
	end

	test "Map.put" do
		assert Map.put(sample, :foo, 'bob') == %{foo: 'bob', baz: 'quz'}
		assert Map.put(sample, :far, 'bar') == %{foo: 'bob', baz: 'quz', far: 'bar'}
	end
end
