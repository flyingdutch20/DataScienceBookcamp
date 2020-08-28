sample_space = {'Heads', 'Tails'}
probability_heads = 1 / len(sample_space)
print(f'Probability of choosing heads is {probability_heads}')

def is_heads_or_tails(outcome):  return outcome in {'Heads', 'Tails'}
def is_neither(outcome): return not is_heads_or_tails(outcome)

def is_heads(outcome): return outcome == 'Heads'
def is_tails(outcome): return outcome == 'Tails'

def get_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space
                if event_condition(outcome)])