class RabinKarp:

    """
        Constructor initialising the modulo value, if any.
        @ param mod_val - Modulo value to be used for hashing, if provided.
    """

    def __init__(self, mod_val = None):
        self.textlen = None
        self.patterlen = None
        self.mod_val = mod_val
        self.base = 29


    def search(self, pattern, text):
        """
        This method uses the RabinKarp algorithm to search a given pattern in a given input text.
        @ param pattern - The string pattern that is searched in the text.
        @ param text - The text string in which the pattern is searched.
        @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
        @ raises ValueError if pattern or text is None or empty."""

        if pattern is None or pattern == "" or text == "" or text is None:
            raise ValueError

        pattern = str(pattern)
        pattern_hash = self.get_hash(pattern)

        self.textlen = len(text)
        self.patterlen = len(pattern)

        res_idx = []

        comp_hash = None
        last_char = None

        for idx in range(self.textlen+1-self.patterlen):
            seq = text[idx:idx + self.patterlen]
            comp_hash = self.get_rolling_hash_value(seq, last_char, comp_hash)
            last_char = seq[0]

            if comp_hash == pattern_hash:
                if seq == pattern:
                    res_idx.append(idx)

        print(res_idx)
        return res_idx

    def get_rolling_hash_value(self, sequence, last_character, previous_hash):
        """
        This method calculates the (rolling) hash code for a given character sequence. For the calculation use the base b=29.
        @ param sequence - The char sequence for which the (rolling) hash shall be computed.
        @ param lastCharacter - The character to be removed from the hash when a new character is added.
        @ param previousHash - The most recent hash value to be reused in the new hash value.
        @ return hash value for the given character sequence using base 29."""

        if previous_hash == None or previous_hash == 0:
            return self.get_hash(sequence)
        else:
            return previous_hash*29-ord(last_character)*29**self.patterlen + ord(sequence[self.patterlen-1])

    def get_hash(self, pattern: str):
        """calculating hash_value of string, either with or without modulo value"""

        asc_codes = []
        idx = 1
        self.patterlen = len(pattern)

        hash_val = 0
        if self.mod_val is not None:
            hash_list = []
            for char in pattern:
                asc = ord(char)
                hash_list.append((self.base ** (self.patterlen - idx) * asc) % self.mod_val)
            hash_val = sum(hash_list) % self.mod_val

        else:
            for char in pattern:
                asc = ord(char)
                asc_codes.append(asc)
                hash_val = hash_val + self.base ** (self.patterlen - idx) * asc
                idx += 1

        return hash_val

rkarp = RabinKarp(mod_val= 1119)
hs = rkarp.get_hash('abwstasdfaserwerqhsadfgasdfaasdfjölqwjeroiju')
print(str(hs))
