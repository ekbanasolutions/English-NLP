from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
import os
from collections import defaultdict
from typing import Any, Optional, Text, Dict
import numpy as np
import Levenshtein
from nltk.corpus import stopwords

stopwords = list(set(stopwords.words('english')))

def auto_correct(check_word, list_of_words):
    """
    :param check_word: either a string or a list of word to check the spelling
    :param list_of_words: a list of valid word ( litttle corpse ) for spell checking
    :return: same check_word but in corrected form
    """
    ## autocorrection code here using laveshtein
    pass
class AutocorrectNouns(Component):
    """A pre-trained sentiment component"""

    name = "autocorrect_nouns"
    provides = ["entities"]
    requires = []
    ## add the entities in defaults for which you want autocorrection.
    defaults = {"lookup":["horoscopelist"]}
    language_list = ["en"]

    def __init__(self, component_config=None):
        super(AutocorrectNouns, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        ## but you can select lookups for which autocorrect is needed
        pass

    def convert_to_rasa(self, suggestions):
        """Convert model output into the Rasa NLU compatible output format."""
        entities = []
        for each in suggestions:
            entities.append({"value": each["value"],
                  "confidence": each["confidence"],
                  "entity": "autocorrect_nouns"+ "_" + each["entity"], 
                  "extractor": "AutocorrectNoun"})

        return entities


    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""
        
        suggestions = []
        text = message.text
        # get suggestion by passing text to autocorrect and store in suggestion
        # extract autocorrected entities and send to convert_to_rasa
        entities = self.convert_to_rasa(suggestions)
        message.set("entities", entities, add_to_output=True)


    def persist(self, file_name, model_dir):
        """"""
        # saving your model of this file as python object
        classifier_file = os.path.join(model_dir, "entites_autocorrect.pkl")
        utils.json_pickle(classifier_file, self)
        return {"autocorrect_file": "entites_autocorrect.pkl"}

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir=None,
             model_metadata=None,
             cached_component=None,
             **kwargs):
        file_name = meta.get("autocorrect_file")
        classifier_file = os.path.join(model_dir, file_name)
        return utils.json_unpickle(classifier_file)
