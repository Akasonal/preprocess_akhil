from preprocess_akhil import utils
__version__='0.001'


def word_count(x):
	return utils.word_count(x)

def char_count(x):
	return utils.char_count(x)

def avg_word_count(x):
	return utils.avg_word_count(x)

def stop_word_count(x):
	return utils.stop_word_count(x)

def hashtag_count(x):
	return utils.hashtag_count(x)

def mention_count(x):
	return utils.mention_count(x)

def numeric_digit_count(x):
	return utils.numeric_digit_count(x)

def upper_case_count(x):
	return utils.upper_case_count(x)

def lower_case_conversion(x):
	return utils.lower_case_conversion(x)

def cont_to_exp(x):
	retutn utils.cont_to_exp(x)

def _get_emails(x):
	return utils._get_emails(x)

def email_removal(x):
	return utils.email_removal(x)

def _get_url(x):
	return utils._get_url(x)

def remove_url(x):
	return utils.remove_url(x)

def retweet_removal(x):
	return utils.retweet_removal(x)

def remove_spec_char(x):
	return utils.remove_spec_char(x)

def remove_mul_space(x):
	return utils.remove_mul_space(x)

def remove_html_tag(x):
	return utils.remove_html_tag(x)

def remove_ac_char(x):
	return utils.remove_ac_char(x)

def remove_stop_words(x):
	return utilsremove_stop_words(x)

def base_root_form(x):
	return utils.base_root_form(x)

def remove_common_words(x,num=20):
	return utils.remove_common_words(x,num=20)

def remove_rare_words(x,num=20):
	return utils.remove_rare_words(x,num=20)


def spelling_correction(x):
	return utils.spelling_correction(x)











