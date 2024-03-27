import random
import emoji
print(''.join([random.choice(emoji.UNICODE_EMOJI.keys()) for _ in range(1000)]))
