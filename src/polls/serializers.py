from rest_framework import serializers

from .models import Poll, Question, Answer, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='text')

    class Meta:
        model = Choice
        fields = '__all__'

    def validate(self, attrs):
        try:
            obj = Choice.objects.get(question=attrs['question'].id, text=attrs['text'])
        except Choice.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Choice already exists')

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='title')
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def validate(self, attrs):
        question_type = attrs['type']
        if question_type == 'one' or question_type == 'multiple' or question_type == 'text':
            return attrs
        raise serializers.ValidationError('Question type can be only one, multiple, text')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='text')
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='title')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='text')

    class Meta:
        model = Answer
        fields = ('text_vote', 'question', 'poll', 'user', 'choice', )

    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs['question'].id).type
        try:
            if question_type == "one" or question_type == "text":
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user=attrs['user'])
            elif question_type == "multiple":
                obj = Answer.objects.get(question=attrs['question'].id, poll=attrs['poll'], user=attrs['user'],
                                         choice=attrs['choice'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Already responded')

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance