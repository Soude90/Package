from text_preprocessing import utils

__version__='0.0.1'

def strip_accents(text):
	return utils._strip_accents(text)

def spell_check(x):
	return utils._spell_check(x)

def remove_space(x):
	return utils._remove_space(x)

# Expanding the contracted words
def contration_to_expansion(x):
	return utils._contration_to_expansion(x)

# Removing Puntuation 
def puntuation_removal(x):
	return utils._puntuation_removal(x)

# converting to base form
def make_to_base(x):
	return utils._make_to_base(x)

# Removing the emails
def remove_emails(x):
	return utils._remove_emails(x)

# Removing urls
def remove_urls(x):
	return utils._remove_urls(x)


# Creating tokens
def tokenize(x):
	return utils._tokenize(x)

# Remove stopwords
def remove_stopwords(x):
	return utils._remove_stopwords(x)