"""

A simple version of the number-to-position experiment: 
- -1 to 1 number line
- The color of the feedback arrow changes according to the response accuracy (endpoint error), 
  and so does the acknowledgement sound.
- The correct location is shown with the feedback

@author: Dror Dotan
@copyright: Copyright (c) 2017, Dror Dotan
"""

import expyriment as xpy

import trajtracker as ttrk
import trajtrackerp as ttrkp
from trajtrackerp import num2pos, common


#-- Change this to True to switch into stimulus-then-move mode
STIMULUS_THEN_MOVE = False

if not xpy.misc.is_android_running():
    xpy.control.defaults.window_mode = True
    ttrk.log_to_console = True

ttrk.env.default_log_level = ttrk.log_info


accuracy_levels = [.05, .1]

config = num2pos.Config("Num2Pos(D+U)",
                        use_generic_targets=True,
                        use_text_targets=False,
                        stimulus_then_move=STIMULUS_THEN_MOVE,
                        min_inst_speed=1,
                        max_movement_time=10, # Number of seconds for max response time
                        speed_guide_enabled=True,
                        shuffle_trials=False,
                        max_offscreen_duration=1,
                        min_numberline_value=0, # Left endpoint of number line
                        max_numberline_value=1, # Right endpoint of number line
                        data_source="fraction_to_position_2019.csv",  # Read targets from this CSV file
    

                        fixation_type='cross',

                        post_response_target=False,         # After response was made, show the correct location (could be T or F)
                        # feedback_arrow_colors=[xpy.misc.constants.C_GREEN,
                        #                       xpy.misc.constants.C_EXPYRIMENT_ORANGE,
                        #                       xpy.misc.constants.C_RED],
                        feedback_accuracy_levels=accuracy_levels,
                        # sound_by_accuracy=((accuracy_levels[0], 'feedback-accuracy-0.wav'),
                        #                    (accuracy_levels[1], 'feedback-accuracy-1.wav'),
                        #                    (1, 'feedback-accuracy-2.wav'))
                        )

#----------------------------------------------------------------

#-- Initialize & start the Expyriment
exp = ttrk.initialize()

xpy.control.start(exp)

if not xpy.misc.is_android_running():
    exp.mouse.show_cursor()

#-- Get subject info
(subj_id, subj_name) = ttrkp.common.get_subject_name_id()


#-- Define stimuli

stimuli = {
    '1_6': xpy.stimuli.Picture("./fractions/1_6.png"),
    '1_9': xpy.stimuli.Picture("./fractions/1_9.png"),
    '3_8': xpy.stimuli.Picture("./fractions/3_8.png"),
    '4_5': xpy.stimuli.Picture("./fractions/4_5.png"),
    '7_15': xpy.stimuli.Picture("./fractions/7_15.png"),
    '10_13': xpy.stimuli.Picture("./fractions/10_13.png"),
    '10_19': xpy.stimuli.Picture("./fractions/10_19.png"),
    '11_12': xpy.stimuli.Picture("./fractions/11_12.png"),
    '1_17': xpy.stimuli.Picture("./fractions/1_17.png"),
    '11_35': xpy.stimuli.Picture("./fractions/11_35.png"),
    '16_25': xpy.stimuli.Picture("./fractions/16_25.png"),
    '28_109': xpy.stimuli.Picture("./fractions/28_109.png"),
    '120_553': xpy.stimuli.Picture("./fractions/120_553.png"),
    '291_491': xpy.stimuli.Picture("./fractions/291_491.png"),
    '703_891': xpy.stimuli.Picture("./fractions/703_891.png"),
}
    


#-- Initialize the experiment objects

exp_info = num2pos.ExperimentInfo(config, exp, subj_id, subj_name)
num2pos.create_experiment_objects(exp_info)

#exp_info.text_target.onset_time = [0, 0.1]
#exp_info.text_target.duration = [10, 20]

common.register_to_event_manager(exp_info)

#-- Use defined generic Stimuli

exp_info.generic_target.available_stimuli = stimuli

#-- Run the experiment
num2pos.run_trials(exp_info)

#-- Shutdown Expyriment
xpy.control.end()
