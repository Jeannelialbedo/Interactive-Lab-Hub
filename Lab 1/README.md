

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.



For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_

# *Abetes*: Domestic Urinalysis Device for Diabetic Testing. Testing with only 1 drop of urine.
![logo](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/logo.png)
![logo UI](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/logo%20UI.png)

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.
**Describe your setting, players, activity and goals here.**

**Mio's family used to be happy until recently her dad was diagnosed to have high risk of becoming a diabetic. A even worse scenario was that Mio might have inherited diabetes from her dad. Keeping track of the potential patients' glucose was indispensable. However, it would undoubtedly be extemely inconvenient for the family to go to the hospital frequently and take urinalysis or glucose test, especially when it was during the pandemic social distancing.**

**To solve the problem, I invented *Abetes* -- a domestic urinalysis device for diabetic Testing. The mini portable device could be placed at home. It could also easily be carried with the patients when they are out.  Input: The device could test the glucose of the patient with only 1 drop of urine. Output: When the test-taker drops the urine onto the glass of the device at home, if there is low risk of diabetes, it turns green with a "ding" sound, meaning the test-taker is totally safe. When there flashes orange light with a warning "danger" sound, it demonstrates that the test-taker is at intermediate risk. The worst case, when it presents red with a frightened "gong" sound, it suggests that the test-taker is at high risk. And it is urgent for the test-taker to visit his or her doctor and take treatments and medication.**

**The interactive device connects with the smartphones and computers of the patients, family members, and the doctors, allowing them to track the daily change of the patient's glucose. Once the intermediate-risk patient becomes high-risk, or the high-risk patient becomes worse, the hospital would take actions to give patients treatments and hospitalization. It proffers glucose testing and home hospitalization anytime and anywhere.**

Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 
**Include a picture of your storyboard here**
![storyboard](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/storyboard.jpg)

Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.
**Summarize feedback you got here.**
**My classmates in my classroom love the idea that it actually solve urgent medical issues with a portable device. The device originally only presents color switch. They gave me advice on combining alarm sound with the colors to demonstrate greater attention on the high risk.**

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**
**When working with a paper prototype, it natively achieve the goal of being "portable". Also, the nature of paper made if more like a glucose testing strips (already exist in the market) rather than some interactive device. Therefore, when I actually fabricate the real device, I must first consider the size of it. **

**Are there new ideas that occur to you or your collaborators that come up from the acting?**
**After acting with my collaborators, I also added a google cardboard as a holder of the responsive device (referring to smarphone here) and a arduino board to have it serve as the internal testing device. These moves highlighted the "interactive" part as well as the "device" part. Because it could indeed respond to the one drop of urine.**

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 
**Give us feedback on Tinkerbelle.**
**Sound could be more diverse. It would be better if I type in "Dangerous", and it would pronounce the same word.**

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**
**The set-up tinkerbelle video:https://drive.google.com/file/d/1WsYcZbfTxrckNcPcUW6RcVo04wUNebg8/view?usp=sharing (This is the only link I added after 11:25am because I put in a wrong one)**
**The set-up device video:https://drive.google.com/file/d/1loWJlK6Zcpz8WMu2lzTzaVVdT58PVejy/view?usp=sharing**

**low risk green**![low risk green](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/low%20risk%20green.png)
**intermediate risk orange**![intermediate risk orange](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/intermediate%20risk%20orange.png)
**high risk red**![high risk red](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/high%20risk%20red.png)
Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**
**Paper prototype for better understanding the implementation process:https://drive.google.com/file/d/1BxM38rIp72qFj03S8Kzf1O6m2hNbWTDr/view?usp=sharing**

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**
![device sketch](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/device%20sketch.jpg)
![costumed device](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/photos%20of%20costumed%20device.jpg)
![costumed device1](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/photos%20of%20costumed%20device%202.jpg)
![costumed device2](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/photos%20of%20costumed%20device%203.jpg)
![costumed device3](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/photos%20of%20costumed%20device%204.jpg)
![costumed device4](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/photos%20of%20costumed%20device%205.jpg)

**What concerns or opportunitities are influencing the way you've designed the device to look?**
**Currently the input would be 1 drop of urine, and the output would be the color and the sound. I am thinking of making it more a personalized toolkit, giving feedbacks to the patient. And the sound could sounds like family members'**

## Part F. Record

**Take a video of your prototyped interaction.**

The final interaction video:https://drive.google.com/file/d/1BcZWWnbL6PJKVV8SlP0FXy1fvwXi_IKK/view?usp=sharing

**Please indicate anyone you collaborated with on this Lab.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

**I would say thank you to my iTrek team for inspiring me on creating digital health devices. We made a domestic portable digital pillbox Minder for elderly patients during the pandemic social distancing. And we won the second prize. This is the starting point of me perceiving medical tech issues as one of the most pivotal social missions.**

**Furthermore, as I started researching on portable devices for diabetic test, there were merely testing strips (https://shop.keto-mojo.com/products/keto-mojo-gk-plus-ketone-test-strips-60-pack?variant=32785665785961&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gclid=EAIaIQobChMI1Mmt2JDs7gIV0ACtBh35Fw36EAYYBSABEgK60fD_BwE). Another glucose monitoring device(https://intro.mydario.com/DarioGlucoseMeter/pay-on-shop-d.php?tid=google.Dario_US_Shopping_MCPC_11.701&utm_source=google&utm_medium=cpc&utm_campaign=Dario_US_Shopping_MCPC_11&utm_content=701&gclid=EAIaIQobChMI1Mmt2JDs7gIV0ACtBh35Fw36EAYYAiABEgIH1vD_BwE) which connects with the smartphones also enlighted me during ideation.**

# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

**Summarize feedback from your partners here.**

**Jiadong Lou (jl3937): By just looking at the title of the GitHub page and the video, I have already understood clearly the purpose of the device. It’s very clear for me that the scene is about testing for diabetes. The goal of the character is to get a rapid test result for diabetes. The choice of color can intuitively reflects the result of the test without even explaining to the user. Therefore, I think it’s a very well designed interactive device. I would suggest that to add another color that indicates invalid test samples. What if the user drops water instead of urine? You can add a new color to ask the user to try again(error prevention). Overall, very good work!**

**Chelsea Luo (cl773): This is a really cool design, and I could see the idea being utilized widely. The video clearly demonstrates the idea, and the costume of the device is very well made. I like how you not only incorporated color for the visual feedback but also utilized different audio sources to convey different messages. Since there are three different potential feedbacks, it might be good to use more specific text-to-voice to differentiate the meaning behind each color (I know it is difficult to do with Tinkerbelle).**

**Yuanhao zhu (yz2696): From the video, I saw the user need to pour their urine sample on the device, and then the device will give an evaluation of diabetes based on the urine color. The idea is cool and I can see the great potential of this device. The color feedback is intuitive, as red represents high risk and green for low risk. The sound notification adapts to the color blind and other disability populations. The only thing that’s not clear is that the box has two wells for a urine sample, but in the video the user only used one, so is there any reason that there are two wells? Or it’s just because the box is made from a pair of goggles?**

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors, 
3) We will be grading with an emphasis on creativity. 

**Document everything here.**
## Part A. Plan 

**Iteration - New Features:**
**1. Large hardware with glasses changed to portable testing paper**
**2. Personalized test and pill taking reminder with cute avatars that could be customized by the user**
**3. User's behavioral data including daily emotion and sleeping pattern tracked**
**4. Tinkerbelle changed to Arduino light and buzzer**

**Describe your setting, players, activity and goals here.**

**Suzie, 24, was diagnosed to have high risk of diabetes due to genetic reasons. She was asked by her doctor to keep track of her glucose frequently. Nonetheless, during the pandemic, she was not capable of going to the hospital and take urinalysis everyday. So the hospial gave her a smart urinalysis kit - *Abetes*. It allows her to easily collect urine samples every morning when toileting.**

**I invented *Abetes* -- a domestic urinalysis device for diabetic Testing. The mini portable device could be placed at home. It could also easily be carried with the patients when they are out.  Input: The device could test the glucose of the patient with only 1 drop of urine on the testing paper. Output: When the test-taker drops the urine onto the testing paper, if there is low risk of diabetes, it shows a "smiley face" with a low sound, meaning the test-taker is totally safe. When there showed a "unhappy face" with a warning intermittent higher sound, it demonstrates that the test-taker is at intermediate risk. The worst case, when it presents a "deeply-sad face" with a frightened continuous higher sound, it suggests that the test-taker is at high risk. And it is urgent for the test-taker to visit his or her doctor and take treatments and medication.**

**Moreover, *Abetes* is synthesized with the user's daily toileting routine, helping the user to naturally develop a testing habbit. It proffers personalized test and pill taking reminder with cute avatars. It also collects User's behavioral data including daily emotion and sleeping pattern.**

**The interactive device connects with the smartphones and computers of the patients, family members, and the doctors, allowing them to track the daily changes and behavioral patterns of the patient's glucose. Once the intermediate-risk patient becomes high-risk, or the high-risk patient becomes worse, the hospital would take actions to give patients treatments and hospitalization. It proffers glucose testing and home hospitalization anytime and anywhere.**

**The *Abetes* smart kit also support family use. Mio's family used to be happy until recently her dad was diagnosed to have high risk of becoming a diabetic. A even worse scenario was that Mio might have inherited diabetes from her dad. Keeping track of the potential patients' glucose was indispensable. However, it would undoubtedly be extemely inconvenient for the family to go to the hospital frequently and take urinalysis or glucose test, especially when it was during the pandemic social distancing.**


**Include a picture of your storyboard here**
![storyboard](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20storyboard.jpg)

**Summarize feedback you got here.**

**My breakout roommates thought this smart kit was even more accessible and portable than version 1. Especially when it is integrated with the user's daily routine, e.g. toileting, it makes the user more willing to employ the testing toilet paper. The personalized features are also super cute!**

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

**Are there things that seemed better on paper than acted out?**

**When working with a paper prototype, it is quite easy to create a fusion of the input testing paper and the output tesing device. However, when actually fabricating the kit, it seemed hard to amalgmate all the functionalities in one piece of toilet paper. So the toilet paper is not so "smart" as it should have been. **

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

**At first, I was thinking of creating another device to substitute the Google goggle in version 1 - perhaps a even more complex and cumbersome one. After acting with my collaborators, I was inspired that the product could follow the intrinsic logic of the natural urine collecting process - toileting. And the device could be the convenient toilet paper.**

## Part C. Prototype the device


**Arduino buzzer & light code** ![arduino code](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20arduino%20code.png)

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

**Include your first attempts at recording the set-up video here.**
**The set-up device video:https://drive.google.com/file/d/17UHWDQMho408qSxVo6wjtfX-oaBbjKPQ/view?usp=sharing**
![setup1](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20setup1.jpg)
![setup2](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20setup2.jpg)

**low risk**![low risk green](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20arduino%20code%20low%20risk.png)

**intermediate risk**![intermediate risk orange](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20arduino%20code%20intermediate%20risk.png)

**high risk**![high risk red](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20arduino%20code%20high%20risk.png)

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

**Show the follow-up work here.**

**Paper prototype for better understanding the implementation process:https://drive.google.com/file/d/118APwxm_p6nc3f10KMt51o427PXRlDwp/view?usp=sharing**

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

**Include sketches of what your device might look like here.**
![device sketch0](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20device%20sketch0.jpg)
![device sketch1](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20device%20sketch1.jpg)
![device sketch2](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20device%20sketch2.jpg)
![device sketch3](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20device%20sketch3.jpg)
![device sketch4](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20device%20sketch4.jpg)
![device sketch5](https://github.com/Jeannelialbedo/Interactive-Lab-Hub/blob/Spring2021/Lab%201/1.2%20device%20sketch5.jpg)

**What concerns or opportunitities are influencing the way you've designed the device to look?**

**In version 1, I was thinking of making it more a personalized toolkit, giving feedbacks to the patient. So I added the cute avatar which could be customized by the user. The toilet paper as the testing device making it more convenient and accessible for the user to form a habbit.**

## Part F. Record

**Take a video of your prototyped interaction.**

**The final interaction video:https://drive.google.com/file/d/1zbhDeHk_g_n9tw7aO6217eiyKrYBBwUq/view?usp=sharing**

**Please indicate anyone you collaborated with on this Lab.**

**I would say thank you to classmates, Chelsea, Jiadong, Yuanhao, who gave me extremely enlightening feedback of version 1.**
