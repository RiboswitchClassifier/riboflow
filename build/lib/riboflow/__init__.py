# Import Libraries
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pkg_resources

# Names of 24 riboswitches
riboswitch_names = [
    'RF00050 - Flavin Mononucleotide Riboswitch',
    'RF00059 - Thiamine pyrophosphate riboswitch',
    'RF00162 - SAM - 1 Riboswitch',
    'RF00167 - Purine Riboswitch',
    'RF00168 - Lysine Riboswitch',
    'RF00174 - Cobalamin riboswitch',
    'RF00234 - Glucosamine-6-phosphate riboswitch',
    'RF00380 - Ykok riboswitch(Magnesium sensing riboswitch)',
    'RF00504 - Glycine riboswitch',
    'RF00521 - SAM - 2 Riboswitch',
    'RF00522 - pre-queosine riboswitch1',
    'RF00634 - SAM - 4 Riboswitch',
    'RF01051 - Cyclic di-GMP-I riboswitches',
    'RF01054 - pre-queosine riboswitch2',
    'RF01055 - Molybdenum Co-factor riboswitch',
    'RF01057 - SAH Riboswitch',
    'RF01725 - SAM -1 -4 Variant riboswitch',
    'RF01726 - SAM - 2 Long loop riboswitch',
    'RF01727 - SAM-SAH Riboswitch',
    'RF01734 - Fluoride Riboswitch',
    'RF01739 - Glutamine riboswitch',
    'RF01763 - Guanidine - 3 Riboswitch',
    'RF01767 - SAM - 3 Riboswitch',
    'RF02683 - NiCo riboswitch(sense Nickel or Cobalt)'
]

# Convert the letters to numerical format
def letter_to_index(letter):
    alphabets = 'ATGCN'
    if letter not in alphabets:
        return None, letter
    else:
        return next((i for i, _letter in enumerate(alphabets) if _letter == letter), None)

# Check if the sequneces have only alphabets present
def check_isalpha(sequences):
    for sequence in sequences:
        if not sequence.isalpha():
            return None, sequence
    return sequences, None

# Perform Charecter Mapping
def clean_sequnces(sequences):
    existing_letter = ['R', 'Y', 'M', 'K', 'S', 'W', 'H', 'B', 'V', 'D']
    new_letter      = ['G', 'T', 'A', 'G', 'G', 'A', 'A', 'G', 'G', 'G']
    length_sequences = len(sequences)
    for old, new in zip(existing_letter, new_letter):
        for i in range(length_sequences): 
            sequences[i] = sequences[i].replace(old, new)
    return sequences

# Check if Only supported charecters exist
def check_supported_charecters(cleaned_sequences):
    for sequence in cleaned_sequences:
        valid = set(sequence).issubset('ATGCN')
        if valid == False:
            return None, sequence
    return cleaned_sequences, None 

# Format the Sequence
def format_sequences(sequences):
    max_sequence_len = 250
    formatted_sequence = []
    for sequence in sequences:
        formatted_sequence.append([int(letter_to_index(charecter)) for charecter in sequence ])
    formatted_sequence = np.array(formatted_sequence)
    return pad_sequences(formatted_sequence, maxlen = max_sequence_len)

# Construct the final output hash for probabilty for each riboswitch label
def construct_output(class_wise_probabilty):
    result = []
    for riboswitch_classes in class_wise_probabilty:
        output = []
        count = 1
        for riboswitch_class, name in zip(riboswitch_classes, riboswitch_names):
            sequence_component = {}
            sequence_component["name"] = name
            sequence_component["label"] = count
            sequence_component["probability"] = riboswitch_class
            count += 1
            output.append(sequence_component)
        result.append(output)
    return result

# Load the Model    
def load_riboswitch_model():
    path = "rnn_24_model.h5"
    filepath = pkg_resources.resource_filename(__name__, path)
    model_loaded = load_model(filepath)
    return model_loaded    

# Perform Predict Class
def perform_predict_class(formatted_sequence, model_loaded):
    result = [] 
    outputs = model_loaded.predict_classes(formatted_sequence)
    for output in outputs:
        component = {}
        component["name"] = riboswitch_names[output]
        component["label"] = output + 1
        result.append(component)
    return result    

# Perform Class Wise Probability Prediction
def class_wise_probabilty_prediction(formatted_sequence, model_loaded):
    class_wise_probabilty = model_loaded.predict(formatted_sequence)
    result = construct_output(class_wise_probabilty) 
    return result

# Choose between two functions "predict_class" or "predict_prob"
def make_prediction(formatted_sequence,option):
    model_loaded = load_riboswitch_model()
    # Predict the label
    if option == "predict_class":
        result = perform_predict_class(formatted_sequence, model_loaded)
    # Predict the probabilty of all labels
    elif option == "predict_prob":
        result = class_wise_probabilty_prediction(formatted_sequence, model_loaded)
    # Unkown 2nd argument passed by the user
    else:
        result = "Unkown Option - Please pass 'predict_class' or 'predict_prob' as the second argument to the predict function"
    return result

def check_arguments_meet_minimum_requirements(sequences, option):
    result = ""
    if (not isinstance(sequences, list)):
        result += "The first argument passed to the 'predict' function needs to be an array of riboswitch sequences."
    if (not isinstance(option, str)):
        result += "The second argument passed to the 'predict' function needs to be a String (One of the two given below):\n1.predict_class\n2.predict_prob."
    if not result:
        return None
    else:
        return result

# Predict the label for the given Riboswitch Sequences 
def predict(sequences,option="predict_class"):
    result = None
    try:
        result = check_arguments_meet_minimum_requirements(sequences, option)
        if result is None:
            sequences, error = check_isalpha(sequences) 
            if sequences is None:
                result = "The sequnece '" + error + "' contains a non-alphabet"  
            else:
                cleaned_sequences = clean_sequnces(sequences)
                cleaned_sequences, error_sequence = check_supported_charecters(cleaned_sequences) 
                if cleaned_sequences is None:
                    result = "Charecter not supported. All letters present in the sequence must be in the set G,A,T,C,R,Y,M,K,S,W,H,B,V,D,N. Sequence " + error_sequence + " has an unsupported charecter"            
                else:
                    formatted_sequence= format_sequences(cleaned_sequences)
                    result = make_prediction(formatted_sequence,option)
    except Exception as the_exception:
        result = str(the_exception)
    return result