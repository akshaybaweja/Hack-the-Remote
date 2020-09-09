def scores_to_emotions(scores,normalize=False):
    
    """
        
    Generates the emojies string from an emotions scores dictionary. if the score of the emoji is 0 then no emojie is shown. greater than 0 is represented as follows (<0.34:1,<0.67:2,>=0.67:3).
    
    Parameters:
    
        scores({str,int}): a dictionary of emotions [anger,disgust,fear,joy,sadness,surprise] and a value [0,1] represents the amount of each emotion in that sentence.
        
        normalize(bool): if normalize is True then the scores are normalized relative to the other emotions scores to a value from 0-1 so that all add to 1. otherwise it takes the score as is.
    
    Returns:
    
        emojies_string(str): a string of the generated emojies 
    
    """
    
    # normalize 
    if normalize:
        summ = sum(list(scores.values()))
        scores = {k:v/summ for k,v in scores.items()}
    
    #const
    emotions_emojies = {"anger":"😡","disgust":"🤢","fear":"😨","joy":"😁","sadness":"😞","surprise":"😮"}
    
    #generate emojies string
    emojies_string = ""
    for k,v in scores.items():
        
        num_emo = 0
        if v >= 0.67:
            num_emo = 3
        elif v >= 0.34:
            num_emo = 2
        elif v > 0:
            num_emo = 1

        for i in range(num_emo):
            emojies_string += emotions_emojies[k]
    
    return emojies_string