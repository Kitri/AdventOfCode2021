import submarine
import importlib
importlib.reload(submarine)

class UnitTests:
    def test_main_sweep(df):
        sonar_sweep = submarine.sonar_sweep_basic(df)
        sonar_sweep_shape = sonar_sweep.shape
        depth_calc = sonar_sweep["depth_calculation"].sum()

        expected_depth_calc = 64
        expected_df_shape_after_transform = (10,3)

        assert depth_calc == expected_depth_calc, f"Sum of depth differences expected to be {expected_depth_calc}, but found {depth_calc}"
        assert expected_df_shape_after_transform == sonar_sweep_shape, f"Expected df to be {expected_df_shape_after_transform} (rows, cols) but found {sonar_sweep_shape}" 

    def test_sliding_window_sweep(df):
        sonar_sweep = sonar_sweep_sliding_window(df)
        sonar_sweep_shape = sonar_sweep.shape
        depth_sum = sonar_sweep["depth_sum"].sum()
        depth_calc = sonar_sweep["depth_calculation"].sum()

        expected_depth_sum_sum = 5384 
        expected_depth_calc_sum = 185 
        expected_df_shape_after_transform = (10,6)

        # print(sonar_sweep.columns)

        assert depth_sum == expected_depth_sum_sum, f"Sum of depth sums expected to be {expected_depth_sum_sum}, but found {depth_sum}"
        assert depth_calc == expected_depth_calc_sum, f"Sum of depth differences expected to be {expected_depth_calc_sum}, but found {depth_calc}"
        assert expected_df_shape_after_transform == sonar_sweep_shape, f"Expected df to be {expected_df_shape_after_transform} (rows, cols) but found {sonar_sweep_shape}" 

    def test_dive_forward():
        sub = Submarine(depth=-3, horizontal_position=5, aim=2)
        sub.dive('forward 6')

        expected_result = (9, 11, 2)
        result = (sub.depth, sub.horizontal_position, sub.aim)

        assert result == expected_result, f"Forward: expected {expected_result}, got {result}"

    def test_dive_up():
        sub = Submarine(depth=3, horizontal_position=4, aim=5)
        sub.dive('up 3')

        expected_result = (3, 4, 2)
        result = (sub.depth, sub.horizontal_position, sub.aim)

        assert result == expected_result, f"Up: expected {expected_result}, got {result}"

    def test_dive_down():
        sub = Submarine(depth=3, horizontal_position=4, aim=5)
        sub.dive('down 3')

        expected_result = (3, 4, 8)
        result = (sub.depth, sub.horizontal_position, sub.aim)

        assert result == expected_result, f"Down: expected {expected_result}, got {result}"

    def test_power_consumption(sample_input):
       expected_result =198 

       result = submarine.calculate_power_consumptions(sample_input)

       assert result == expected_result, f"Gamma calculation expected {expected_result}, found {result}"
