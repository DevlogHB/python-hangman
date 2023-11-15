import random;
import hangmane_words 
from hangmant_art import stages, logo


print(logo);

# 설정된 단어 랜덤 표시
choosed_word = random.choice(hangmane_words.word_list);

guessWord =[];
for num in range(len(choosed_word)):
    guessWord.append("_");


livesNum = 6;

endGameChk = False;

# 게임이 완료될 때까지 while 문
while not endGameChk:
    guess = input("Guess a letter: ").lower();

    # 사용자가 알파벳 하나 이상 입력했을때 메시지 처리
    if len(guess) != 1:
        print("Please enter one alphabet.");
    else:
        # 단어에 알파벳이 포함되어 있는지 체크
        livesChk = False;
    
        # 선택한 알파벳이 단어에 포함되어 있으면 메시지 처리
        if guess in guessWord:
            print(f"You've already guessde {guess}");
        
        for index in range(len(choosed_word)):
            word = choosed_word[index];
            if word == guess:
                guessWord[index] = guess;
                livesChk = True; 
            
        # 단어에 알파벳이 포함되어 있지 않아 행맨 표시
        if not livesChk:
            print(f"You geussed {guess}, that's not in the word. You lose a life.");
            livesNum -=1;
            if livesNum == 0:
                print("You lose.");
                endGameChk = True;
        
        print(f"{' '.join(guessWord)}");
        

        if "_" not in guessWord:
            endGameChk = True;
            print("You Win");

        print(stages[livesNum]);  
