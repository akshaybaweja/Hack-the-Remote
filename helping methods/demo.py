# examples of using the helping methods
from helping_methods import scores_to_emotions

# dummy data ( we get if from the emotions API)
emotion_scores={"anger":0,"disgust":0,"fear":0,"joy":0.13447999002654,"sadness":0.022660050917593,"surprise":0.0087308825457527}

#no normalizations
emojies = scores_to_emotions(emotion_scores,normalize=False)
print('normal: {}'.format(emojies))

#with normalization
emojies_normalized = scores_to_emotions(emotion_scores,normalize=True)
print('normalized: {}'.format(emojies_normalized))