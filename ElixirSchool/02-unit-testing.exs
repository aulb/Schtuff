# http://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html
# http://elixir-lang.org/docs/stable/ex_unit/ExUnit.html
ExUnit.start # Setup the test runner

defmodule MyTest do
	use ExUnit.Case

	test 'simple test' do
		assert 1 + 1 + 1 == 3
		assert 1 + 1 > 3

		# failure message example: test_assert expected: 2
		# assert 1 + 1 == 3
		# 1) test_assert (MyTest) expected: 2, to be equal to 3
	end

	test 'refute is opposite of assert' do
		refute 1 + 1 == 3
	end

	# :atom
	test :assert_raise do
		assert_raise ArithmeticError, fn ->
			1 + "x" # int + str
		end
	end

	test "assert_in_delta asserts that val1 and val2 differ by less than delta." do
		assert_in_delta 1, # actual
			5, # exp
			6 # 1 and 5 differ by less than 6
	end
end
