class PlugLead:
    """
    A class to represent an Enigma Machine pluglead.

    ...

    Attributes
    ----------
    pair : str
        pluglead pair

    Methods
    -------
    encode(char):
        Returns the pluglead encoding for a given char.
    """

    def __init__(self, pair):
        """
        Constructs attributes for the PlugLead object.

        Parameters
        ----------
        pair : str
            pluglead pair

        """

        if len(pair) != 2 or min([65 <= ord(char) <= 90 for char in pair]) is False:
            raise ValueError('Invalid PlugLead! PlugLead pair must an uppercase string of length 2')
        self.pair = pair

    def encode(self, char):
        """
        Returns the pluglead encoding for a given char.

        Parameters
        ----------
        char : str
            A char to encode.

        Returns
        -------
        None

        """

        if char == self.pair[0]:
            return self.pair[1]
        elif char == self.pair[1]:
            return self.pair[0]
        else:
            return char


class Plugboard:
    """
    A class to represent an Enigma Machine plugboard.

    ...

    Attributes
    ----------
    plugleads : list
        List of added plugleads

    Methods
    -------
    check_conflicts(PlugLead):
        Checks for conflicts with existing plugleads in the plugboard.

    add(PlugLead):
        Adds a single pluglead to the plugboard.

    add_many(pair_list):
        Adds multiple plugleads to the plugboard.

    remove(pair):
        Removes a pluglead pair from the plugboard.

    encode(letter):
        Returns the pluglead encoding for a given letter.

    show_pairs():
        Returns all current pluglead pairs in the plugboard.

    """

    def __init__(self, pair_list=None):
        """
        Constructs attributes for the plugboard object.

        Parameters
        ----------
        pair_list : list (default=None)
            List of pluglead pairs.

        """

        self.plugleads = []
        if pair_list is not None:
            self.add_many(pair_list)

    def check_conflicts(self, PlugLead):
        """
        Checks for conflicts with existing plugleads in the plugboard.

        Parameters
        ----------
        pair : PlugLead
            A pluglead being added to the plugboard.

        Returns
        -------
        None - Raises ValueError if conflict found.

        """

        if len(self.plugleads) >= 10:
            raise ValueError('Plugboard full! Plugboard only supports up to 10 pairs')

        for plug in self.plugleads:
            if plug.pair[0] in PlugLead.pair or plug.pair[1] in PlugLead.pair:
                raise ValueError(
                    'Plug lead {} conflicts with existing pair, please ensure plug lead pairs are unique'.format(
                        PlugLead.pair))

    def add(self, PlugLead):
        """
        Adds a single pluglead to the plugboard.

        Parameters
        ----------
        pair : PlugLead
            A pluglead being added to the plugboard.

        Returns
        -------
        None

        """

        self.check_conflicts(PlugLead)
        self.plugleads.append(PlugLead)

    def add_many(self, pair_list):
        """
        Adds multiple plugleads to the plugboard.

        Parameters
        ----------
        pair_list : list
            A list of plugleads being added to the plugboard.

        Returns
        -------
        None

        """

        for pair in pair_list:
            plug = PlugLead(pair)
            self.check_conflicts(plug)
            self.plugleads.append(plug)

    def remove(self, pair):
        """
        Removes a pluglead from the plugboard.

        Parameters
        ----------
        pair : str
            A pluglead pair to remove from the plugboard. e.g. 'AB'.

        Returns
        -------
        None

        """

        for plug in self.plugleads:
            if plug.pair == pair:
                self.plugleads.remove(plug)

    def encode(self, letter):
        """
        Returns the pluglead encoding for a given letter.

        Parameters
        ----------
        letter : str
            A letter to encode through the plugboard.

        Returns
        -------
        Encoded letter.

        """

        for plug in self.plugleads:
            if plug.pair[0] == letter or plug.pair[1] == letter:
                return plug.encode(letter)
        return letter

    def show_pairs(self):
        """
        Returns all current pluglead pairs in the plugboard.

        Parameters
        ----------
        None

        Returns
        -------
        List of pluglead pairs in the plugboard.

        """

        all_pairs = []
        for plug in self.plugleads:
            all_pairs.append(plug.pair)
        return all_pairs


class Rotor:
    """
    A class to represent an Enigma Machine Rotor.

    ...

    Attributes
    ----------
    rotor_name : str
        Name of rotor
    position : str
        Starting position of rotor (A - Z)
    ring_setting : int
        Ring setting of rotor (0 - 25)
    pins : list
        Rotor pins
    notch : str
        Rotor notch position
    mapping : list
        Rotor mappings

    Methods
    -------
    encode_right_to_left(index_in):
        Encodes a numerical representation of a letter (where 'A'=0 and 'Z'=25)
        right to left through the rotor.

    encode_left_to_right(index_in):
        Encodes a numerical representation of a letter (where 'A'=0 and 'Z'=25)
        left to right through the rotor.

    rotate():
        Rotates the pins and mappings of the rotor by one position.

    check_notch():
        Checks if rotor is in notch position.

    """

    def __init__(self, rotor_name, position='A', ring_setting=0):
        """
        Constructs attributes for the rotor object.

        Parameters
        ----------
        rotor_name : str
            Name of rotor
        position : str (default='A')
            Starting position of rotor (A - Z)
        ring_setting : int (default=0)
            Ring setting of rotor (0 - 25)

        """

        self.rotor_name = rotor_name
        self.position = position
        self.ring_setting = ring_setting
        self.pins = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        if rotor_name == 'Beta':
            self.notch = ''
            self.mapping = list('LEYJVCNIXWPBQMDRTAKZGFUHOS')
        elif rotor_name == 'Gamma':
            self.notch = ''
            self.mapping = list('FSOKANUERHMBTIYCWLQPZXVGJD')
        elif rotor_name == 'I':
            self.notch = 'Q'
            self.mapping = list('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        elif rotor_name == 'II':
            self.notch = 'E'
            self.mapping = list('AJDKSIRUXBLHWTMCQGZNPYFVOE')
        elif rotor_name == 'III':
            self.notch = 'V'
            self.mapping = list('BDFHJLCPRTXVZNYEIWGAKMUSQO')
        elif rotor_name == 'IV':
            self.notch = 'J'
            self.mapping = list('ESOVPZJAYQUIRHXLNFTGKDCMWB')
        elif rotor_name == 'V':
            self.notch = 'Z'
            self.mapping = list('VZBRGITYUPSDNHLXAWMJQOFECK')
        else:
            raise ValueError('Invalid rotor name. Valid rotor names are Beta, Gamma, I II, III, IV, V')

            # Adjust mapping according to ring setting
        if ring_setting > 1:
            self.mapping = [chr((ord(c) + self.ring_setting - 1) % 65 % 26 + 65) for c in self.mapping]
            for _ in range(self.ring_setting - 1):
                self.mapping = list(self.mapping[-1]) + self.mapping[0:-1]

        # Adjust pins and mapping according to position
        if position != 'A':
            idx = ord(position) - 65
            self.pins = list(self.pins[idx:]) + list(self.pins[:idx])
            self.mapping = list(self.mapping[idx:]) + list(self.mapping[:idx])

    def encode_right_to_left(self, index_in):
        """
        Encodes a numerical representation of a letter (where 'A'=0 and 'Z'=25)
        right to left through the rotor.

        Parameters
        ----------
        index_in : int
            Numerical representation of letter to be encoded through rotor.

        Returns
        -------
        Char and index of encoded letter.

        """

        char_out = self.mapping[index_in]
        index_out = self.pins.index(char_out)
        return char_out, index_out

    def encode_left_to_right(self, index_in):
        """
        Encodes a numerical representation of a letter (where 'A'=0 and 'Z'=25)
        left to right through the rotor.

        Parameters
        ----------
        index_in : int
            Numerical representation of letter to be encoded through rotor.

        Returns
        -------
        Char and index of encoded letter.

        """

        char_pins = self.pins[index_in]
        index_out = self.mapping.index(char_pins)
        char_out = self.pins[index_out]
        return char_out, index_out

    def rotate(self):
        """
        Rotates the pins and mappings of the rotor by one position.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        self.pins = self.pins[1:] + list(self.pins[0])
        self.mapping = self.mapping[1:] + list(self.mapping[0])

    def check_notch(self):
        """
        Checks if rotor is in notch position.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        return self.pins[0] == self.notch


class Reflector(Rotor):
    """
    A class to represent an Enigma Machine reflector. Uses the Rotor class as
    a superclass.

    ...

    Attributes
    ----------
    reflector_name : str
        Name of rotor
    position : str
        Starting position of rotor (A - Z)
    ring_setting : int
        Ring setting of rotor (0 - 25)
    mapping : list
        Reflector mappings
    pins : list
        Reflector pins

    Methods
    -------
    Inherits methods from Rotor superclass.

    """

    def __init__(self, reflector_name):
        self.reflector_name = reflector_name
        self.mapping = []
        self.pins = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        if reflector_name == 'A':
            self.mapping = list('EJMZALYXVBWFCRQUONTSPIKHGD')
        elif reflector_name == 'B':
            self.mapping = list('YRUHQSLDPXNGOKMIEBFZCWVJAT')
        elif reflector_name == 'C':
            self.mapping = list('FVPJIAOYEDRZXWGCTKUQSBNMHL')
        else:
            raise ValueError('Invalid reflector name. Valid reflector names are A, B, C')


class Enigma:
    """
    A class to represent an Enigma Machine and it's components.

    ...

    Attributes
    ----------
    plugboard : PlugBoard
        PlugBoard used in Enigma Machine.
    rotors : list
        List of Rotors used in Enigma Machine.
    reflector : Reflector
        Reflector used in Enigma Machine.

    Methods
    -------
    add_plugboard(plugboard):
        Adds a plugboard to the Enigma Machine.

    drop_plugboard():
        Drops the plugboard from the Enigma Machine.

    add_rotors(rotor_names, positions, ring_settings):
        Adds multiple rotors to the Enigma Machine.

    drop_rotors():
        Drops all rotors from the Enigma Machine.

    add_reflector(reflector):
        Adds a rotor to the Enigma Machine.

    drop_reflector():
        Drops the reflector from the Enigma Machine.

    validate_machine_config():
        Checks that Enigma Machine has necessary and valid components.

    validate_message(message):
        Checks that message is valid before encoding.

    rotate_rotors():
        Rotates Enigma Machine rotors.

    encode_letter(char):
        Encodes a letter by running it through the Enigma Machine.

    encode_message(message):
        Encodes enigma message by running each letter through the Enigma Machine.

    show_plugboard():
        Shows plugboard settings in Enigma Machine.

    show_rotors(starting_config):
        Shows rotor settings in Enigma Machine.

    show_reflector():
        Shows reflector settings in Enigma Machine.

    show_config(starting_config):
        Shows Enigma Machine configuration.

    solve_enigma(encoded_message, crib, plugboard, rotors, positions, reflector, max_iterations)
        Solves a 3 rotor Enigma Machine given a message, a crib and initial Enigma settings (optional).
        Does not solve the plugboard.

    """

    def __init__(self):
        """
        Constructs attributes for the Enigma object.

        Parameters
        ----------
        None

        """

        self.plugboard = None
        self.rotors = []
        self.reflector = None

    def add_plugboard(self, plugboard):
        """
        Adds a plugboard to the Enigma Machine.

        Parameters
        ----------
        Plugboard : list
            List of plugboard pairs to add to the Enigma Machine.

        Returns
        -------
        None

        """

        if self.plugboard is None:
            self.plugboard = Plugboard(plugboard)
        else:
            raise ValueError('Enigma Machine can only have 1 plugboard')

    def drop_plugboard(self):
        """
        Drops the plugboard from the Enigma Machine.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        self.plugboard = None

    def add_rotors(self, rotor_names, positions=None, ring_settings=None):
        """
        Adds multiple rotors to the Enigma Machine.

        Parameters
        ----------
        rotor_names : list
            List of rotor names to add to the Enigma Machine. First item in list
            is the leftmost rotor.
        positions : list (default=None)
            List of positions for the rotors to be added. First item in list
            is the leftmost rotor.
        ring_settings : list (default=None)
            List of ring settings for the rotors to be added. First item in list
            is the leftmost rotor.

        Returns
        -------
        None

        """

        if positions is None:
            positions = ['A'] * len(rotor_names)
        if ring_settings is None:
            ring_settings = [1] * len(rotor_names)

        if min(len(rotor_names), len(positions), len(ring_settings)) \
           != max(len(rotor_names), len(positions), len(ring_settings)):
            raise ValueError('Rotor settings must have consistent lengths')
        elif len(rotor_names) < 3 or len(rotor_names) > 4:
            raise ValueError('Enigma machine can only have 3 or 4 rotors')
        else:
            for i in range(len(rotor_names)):
                self.rotors.append(Rotor(rotor_names[::-1][i], positions[::-1][i], \
                ring_settings[::-1][i]))

    def drop_rotors(self):
        """
        Drops all rotors from the Enigma Machine.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        self.rotors = []

    def add_reflector(self, reflector):
        """
        Adds a reflector to the Enigma Machine.

        Parameters
        ----------
        Reflector : str
             Reflector to add to the Enigma Machine.

        Returns
        -------
        None

        """

        if self.reflector is not None:
            raise ValueError('Enigma Machine can only have 1 reflector')
        self.reflector = Reflector(reflector)

    def drop_reflector(self):
        """
        Drops the reflector from the Enigma Machine.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        self.reflector = None

    def validate_machine_config(self):
        """
        Checks that Enigma Machine has necessary and valid components.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        if len(self.rotors) < 3 or self.reflector is None:
            raise ValueError('Invalid configuration. Enigma Machine must have at least 3 rotors and 1 reflector')

    def validate_message(self, message):
        """
        Checks that message is valid before encoding.

        Parameters
        ----------
        message : str

        Returns
        -------
        None

        """

        for char in message:
            if ord(char) < 65 or ord(char) > 90:
                raise ValueError('Invalid message. Enigma Machine only supports messages composed of uppercase letters')

    def rotate_rotors(self):
        """
        Rotates Enigma Machine rotors.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # Figure out which rotors need to be rotated
        to_rotate = [-1] * len(self.rotors)
        for i, rotor in enumerate(self.rotors):
            # First rotor is always rotated
            if i == 0:
                to_rotate[i] = 1
            # Second and third rotors rotate if they hit the notch, and rotate next rotor
            if rotor.check_notch() and i < 2:
                to_rotate[i] = 1
                to_rotate[i + 1] = 1

        # Rotate rotors
        for i, rotor in enumerate(self.rotors):
            if to_rotate[i] == 1:
                rotor.rotate()

    def encode_char(self, char):
        """
        Encodes a char by running it through the Enigma Machine.

        Parameters
        ----------
        char : str

        Returns
        -------
        Encoded char.

        """

        # Pass char through plugboard
        if self.plugboard is not None:
            char = self.plugboard.encode(char)

        # Convert char to an index
        idx = ord(char) % 65

        # Rotate Rotors
        self.rotate_rotors()

        # Forward pass through rotors
        for i, rotor in enumerate(self.rotors):
            _, idx = rotor.encode_right_to_left(idx)

        # Pass through reflector
        _, idx = self.reflector.encode_right_to_left(idx)

        # Backwards pass through rotors
        for rotor in reversed(self.rotors):
            _, idx = rotor.encode_left_to_right(idx)

        # Output char
        char = chr(65 + idx)

        # Pass char through plugboard
        if self.plugboard is not None:
            char = self.plugboard.encode(char)

        return char

    def encode_message(self, message):
        """
        Encodes enigma message by running each letter through the Enigma Machine.

        Parameters
        ----------
        message : str

        Returns
        -------
        Encoded message.

        """

        self.validate_machine_config()
        self.validate_message(message)
        encoded_message = ''

        for char in message:
            encoded_message += self.encode_char(char)

        return encoded_message

    def show_plugboard(self):
        """
        Shows plugboard settings in Enigma Machine.

        Parameters
        ----------
        None

        Returns
        -------
        Plugboard pairs.

        """

        return self.plugboard.show_pairs()

    def show_rotors(self, starting_config):
        """
        Shows rotor settings in Enigma Machine.

        Parameters
        ----------
        starting_config : bool (default=True)
            Specifies whether to return the rotor starting or current position.

        Returns
        -------
        List of rotor settings.

        """

        rotor_settings = []
        if starting_config is True:
            for rotor in reversed(self.rotors):
                rotor_settings.append((rotor.rotor_name, rotor.position, rotor.ring_setting))
        else:
            for rotor in reversed(self.rotors):
                rotor_settings.append((rotor.rotor_name, rotor.pins[0], rotor.ring_setting))

        return rotor_settings

    def show_reflector(self):
        """
        Shows reflector settings in Enigma Machine.

        Parameters
        ----------
        None

        Returns
        -------
        Reflector name.

        """

        return self.reflector.reflector_name

    def show_config(self, starting_config=True):
        """
        Shows Enigma Machine configuration.

        Parameters
        ----------
        starting_config : bool (default=True)
            Specifies whether to return the starting or current rotor position.

        Returns
        -------
        Dictionary containing Enigma Machine configuration.

        """

        config = {'plugboard': None, 'rotors': None, 'reflector': None}
        if self.plugboard is not None:
            config['plugboard'] = self.plugboard.show_pairs()
        if self.rotors is not None:
            config['rotors'] = self.show_rotors(starting_config=starting_config)
        if self.reflector is not None:
            config['reflector'] = self.show_reflector()

        return config

def solve_enigma(encoded_message, crib, plugboard=None, rot_in=None, pos_in=None,
                 set_in=None, ref_in=None, return_first=True, max_iterations=100000):
        """
        Solves a 3 rotor Enigma Machine given a message, a crib and initial
        Enigma settings (optional). Does not solve the plugboard.

        Parameters
        ----------
        encoded_message : str
            Encoded message to decode.
        crib : str
            Crib in message to aid in decoding.
        plugboard : list (default=None)
            List of known plugboard configuration.
        rot_in : list (default=None)
            List of known rotors.
        pos_in : list (default=None)
            List of known positions.
        set_in : list (default=None)
            List of known ring settings.
        ref_in : str (default=None)
            Known reflector.
        return_first : bool (default=True)
            Option to stop solving when first solution found.
        max_iterations : int (default=100000)
            Maximum number of iterations to run solver loop.

        Returns
        -------
        List of tuples with decoded message(s) and initial Enigma set_in.

        """

        all_rot = ['I', 'II', 'III', 'IV', 'V', 'Beta', 'Gamma']
        all_pos = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        all_set = [x for x in range(1, 27)]
        all_ref = ['A', 'B', 'C']

        # 1. Case where we know everything
        if rot_in is not None and pos_in is not None and set_in is not None and ref_in is not None:
            combinations = (rot0, rot1, rot2, pos0, pos1, pos2, ref) = rot_in[0], rot_in[1], rot_in[2], \
                            pos_in[0], pos_in[1], pos_in[2], set_in[0], set_in[1], set_in[2], \
                            ref_in
            combinations = [list(combinations)]

        # 2. Case where we know rotors, positions and settings
        elif rot_in is not None and pos_in is not None and set_in is not None and ref_in is None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos_in[0], pos_in[1], pos_in[2],
                             set_in[0], set_in[1], set_in[2], ref)
                             for ref in all_ref)

        # 3. Case where we know rotors, positions and reflector
        elif rot_in is not None and pos_in is not None and set_in is None and ref_in is not None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos_in[0], pos_in[1], pos_in[2],
                             set0, set1, set2, ref_in)
                             for set0 in all_set for set1 in all_set for set2 in all_set)

        # 4. Case where we know rotors, settings and reflector
        elif rot_in is not None and pos_in is None and set_in is not None and ref_in is not None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos0, pos1, pos2,
                             set_in[0], set_in[1], set_in[2], ref_in)
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos)

        # 5. Case where we know position, settings and reflector
        elif rot_in is None and pos_in is not None and set_in is not None and ref_in is not None:
            combinations = ((rot0, rot1, rot2, pos_in[0], pos_in[1], pos_in[2],
                             set_in[0], set_in[1], set_in[2], ref_in)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # 6. Case where we know only rotors and positions
        elif rot_in is not None and pos_in is not None and set_in is None and ref_in is None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos_in[0], pos_in[1], pos_in[2],
                             set0, set1, set2, ref)
                             for set0 in all_set for set1 in all_set for set2 in all_set
                             for ref in all_ref)

        # 7. Case where we know only rotors and settings
        elif rot_in is not None and pos_in is None and set_in is not None and ref_in is None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos0, pos1, pos2,
                             set_in[0], set_in[1], set_in[2], ref)
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                             for ref in all_ref)

        # 8. Case where we know only rotors and reflector
        elif rot_in is not None and pos_in is None and set_in is None and ref_in is not None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos0, pos1, pos2,
                             set0, set1, set2, ref_in)
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                             for set0 in all_set for set1 in all_set for set2 in all_set)

        # 9. Case where we know only positions and settings
        elif rot_in is None and pos_in is not None and set_in is not None and ref_in is None:
            combinations = ((rot0, rot1, rot2, pos_in[0], pos_in[1], pos_in[2],
                             set_in[0], set_in[1], set_in[2], ref)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             for ref in all_ref
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # 10. Case where we know only positions and reflector
        elif rot_in is None and pos_in is not None and set_in is None and ref_in is not None:
            combinations = ((rot0, rot1, rot2, pos_in[0], pos_in[1], pos_in[2],
                             set0, set1, set2, ref_in)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             for set0 in all_set for set1 in all_set for set2 in all_set
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # 11. Case where we know only settings and reflector
        elif rot_in is None and pos_in is None and set_in is not None and ref_in is not None:
            combinations = ((rot0, rot1, rot2, pos0, pos1, pos2,
                             set_in[0], set_in[1], set_in[2], ref_in)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # 12. Case where we only know the rotors
        elif rot_in is not None and pos_in is None and set_in is None and ref_in is None:
            combinations = ((rot_in[0], rot_in[1], rot_in[2], pos0, pos1, pos2,
                             set0, set1, set2, ref)
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                             for set0 in all_set for set1 in all_set for set2 in all_set
                             for ref in all_ref)

        # 13. Case where we only know the positions
        elif rot_in is None and pos_in is not None and set_in is None and ref_in is None:
            combinations = ((rot0, rot1, rot2, pos_in[0], pos_in[1], pos_in[2],
                             set0, set1, set2, ref)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             for set0 in all_set for set1 in all_set for set2 in all_set
                             for ref in all_ref
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # 14. Case where we only know the settings
        elif rot_in is None and pos_in is None and set_in is not None and ref_in is None:
            combinations = ((rot0, rot1, rot2, pos0, pos1, pos2,
                             set_in[0], set_in[1], set_in[2], ref)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                             for ref in all_ref
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # 15. Case where we only know the reflector
        elif rot_in is None and pos_in is None and set_in is None and ref_in is not None:
            combinations = ((rot0, rot1, rot2, pos0, pos1, pos2,
                              set0, set1, set2, ref_in)
                             for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                             for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                             for set0 in all_set for set1 in all_set for set2 in all_set
                             if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # Catch-all case where we don't know anything!
        else:
            combinations = ((rot0, rot1, rot2, pos0, pos1, pos2, ref)
                            for rot0 in all_rot for rot1 in all_rot for rot2 in all_rot
                            for pos0 in all_pos for pos1 in all_pos for pos2 in all_pos
                            for ref in all_ref
                            if rot0 != rot1 and rot0 != rot2 and rot1 != rot2)

        # Solve the message
        decoded_messages = []
        iterations = 0

        for comb in combinations:
            if iterations >= max_iterations and max_iterations > 0:
                raise TimeoutError('Maximum iterations reached: {}. Increase max_iterations to \
                                   solve for more iterations'.format(max_iterations))
            my_enigma = Enigma()
            if plugboard is not None:
                my_enigma.add_plugboard(plugboard)
            my_enigma.add_rotors([comb[0], comb[1], comb[2]], [comb[3], comb[4], comb[5]],
                                 [comb[6], comb[7], comb[8]])
            my_enigma.add_reflector(comb[9])
            decoded_message = my_enigma.encode_message(encoded_message)
            iterations += 1
            if decoded_message.find(crib) > -1:
                decoded_messages.append((decoded_message, my_enigma.show_config()))
                if return_first is True:
                    return decoded_messages

        return decoded_messages
