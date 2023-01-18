# Guidance for Video & Report Submission

Kindly note that the DDL for our course project presentation video & report submission is approaching (Dec. 25, 11:00AM). We did see some submission of materials like video recording ahead of time, but might not be that ideal and the quality could be improved. Here we'd like to give you some guidance for promoting your performance in the project. You may put this file (the markdown version uploaded on [Blackboard](https://bb.cuhk.edu.cn/)) to your GitHub repo if you find it useful.

## Presentation Video

The major proposes of the presentation video is for:

1. Substituting the original on-site time-limited presentation
2. Serving as the introduction video for future potential viewers of your repository

For the first point, we want to reach the similar standard that we'd set for on-site presentation, but we will provide some relaxation. For the second point, although currently we've set your repository as private in order to protect your codes from plagiarism, we will make it public so that your classmates and furthermore, some job-interviewer could view your work in the repo. We'd like to give you suggestions for the presentation video in the following sections. Note that when we use the word "submit" within the scope of your GitHub repo, we are meant to say "making commits and pushing them to the remote repository on GitHub", similar for the report.

### Video Recording

For such concerns mentioned about, we suggested that your recording of presentation video follow these itemized regulations:

- Suppose the number of members in your team is $n$, **the duration of your video (in minutes) $x$ should satisfies $n \leq x \leq \left \lceil 3 / 2 \cdot n \right \rceil$** (it's relaxed that in the on-site presentation you'll receive an abrupt-stop after we "hit the bell"; here we'd go through those parts exceeding the time limit though it might be harmful to your grades)
- For cases that you need to do some device switching or other similar time-consuming operations, such part(s) should be waived from the time-limit, i.e. we'd regard it to be rational. If you have time for editing, you are free to cut such part(s) off, but you may also leave it there. See the following terms and you'd understand why.
- You may use **Zoom**/Tencent Meeting/WeMeeting/Zhumu Meeting etc. for **presentation video recording**, as such online meeting softwares allow you to work together remotely since some students might have returned home.
- Don't waste time in video editing (we allow editing as long as you don't revise the contents but just have some simple concatenating of video fractions, and the main goal is to **save your time and focus on the presentation**; if you really have much time, you can make some fine editing like adding the subtitles, but we really think it's not necessary as long as your presentation is fluent and well-organized with clear pronunciation). We expect that you can finish the presentation smoothly.
- Along with the last term, you may just utilize the online meeting software and **directly record those contents you want to share**, and there is always some way to show even the complex functionalities you want to show without editing.
  For example (in Option 1), if you want to show that you may scan some QR-code for virtual payment, you may:

  - Prepare one Laptop/PC, two mobiles (one with Zoom installed)
  - Switch on the camera of the mobile for recording in Zoom, stop other screen sharing and "spotlight for everyone" so that the recording should capture the camera view
  - Finish the procedure of the function point, say "scan $\rightarrow$ pay $\rightarrow$ confirm $\rightarrow$ show updated results".

  It's possible that you'll encounter with other complex functionality like Rollback in Option 3; here we don't traverse all possible cases and please think about some easiest way for achieving your goal to show your functionalities before seeking help of video editing software, so as to **save your time**.

### Presentation Contents

We don't have very rigorous rules considering the contents of your presentation, but for promoting your performance, we still provide our suggestions here:

- In your presentation, you should at least cover the following things:

  - Make a introduction for what you've done: brief for those mentioned in the project description but a bit detailed for those you **additionally finished**. This part has nothing to do with the actual implementation, and it's more like "stating out the functionalities", but it's closely relevant to the next point.
  - Show **what's your design and how you break down the tasks**. For Option 1/2, you're specifically required to recall some important ER design and show relevant diagrams. You might utilize the abstract you've written for first two parts. Note that in this part it could involves some introduction like how you populate the data and whether you make some normalization and indexing in Option 1. For option 3 you may talk about your new design if you didn't adapt the original backbone.
  - **List out and show the functionalities** you designed and implemented: you may use the outline-explanation structure, with an outline page listing the important sections, and section pages (it's even okay for "one section title per section page", which can separate the timeline explicitly) for showing the start of explanation for some (bunch of) function(s). In this part, you need to be careful that:
    - You do show the **real-time execution results** of the functionality you introduced. We expect that you can show the execution result right after each recall of functional point/analysis target (i.e. do tell the point you want to show rather than execute everything without any voiceover).
    - You do cover the **minimum requirement** show in the project description to consider your work as complete.
  - Give a summary for what you utilized from those you learnt in the lectures, and show if there is any promotion you want to make in the future.

  Furthermore but optionally, you may make some "code review" (although we can't interact with you since it's not on-site) mainly to show that your implementation are of good logic that meets the requirement. You are welcome to share your insight, and this could be helpful as **high marks require high consistency in presentation and implementation** (i.e. your codes can achieve the degree of perfection you claim in the presentation), and your convincing work can help the TA to check more efficiently.
- It's very recommended that you have some outline page and presentation-progress hinting page (not just for those functionalities you want to show, but for the whole presentation), so that the TA and other potential audience can keep track of your presentation and not lose the focus easily. Also recommended to add page number for some quick reference concerns (it's even more important in real-time presentation).
- For your slides, use the `.pdf` file rather than the `.pptx` file. Make it simple and it just serves as hints for the audience to know what point you've reached. Another advantage is that it could be previewed directly on GitHub.
- As you need to switch between the slides and the program executed in real-time, you may try the way to prepare one device specifically for slides-playing, and turn on "any one in the meeting room can share the screen" as well as "any one can interrupt others' sharing". Hereby, you actually show the program execution in other device(s) and can move back to the slides quickly by "switching between sharing of screens in different devices" rather than "switching between full screen programs in one single device".
- Some team appeared very productive and left a deep impression to the teaching staff, but a problem they might encounter is that the provided time budget is "too limited" that they can not show all the results. In this case, we don't want to break the rules, but you may pick those contents that you think would be most attractive and make your work different for explaining in details. Don't forget to mention that you did finish those "simple" parts even though you're not gonna introduce them in long sentences.
- Some team might really feal not confident enough in their real-time presentation skills. Here we provide an exception that you can use the `.pptx` file, in which you can plugin some fragment of video for each functionality recalled. Hence, you may polish your explanation in each fragment, and merge them into one single powerpoint file, and click "playing" for each functionality you want to introduce. However, you still need to submit a `.pdf` version (see the following sub-section).
- The manuscript you prepare for the presentation will not be wasted -- it can be utilized the report. You may check the paragraph about report guidance for details.

### Video Link & Slides Submission

You don't have to submit the video and slides on BB. Just commit and push them on GitHub. However, please check the following guidance:

- **Do not directly store your presentation video (especially those huge one) on GitHub**, considering that GitHub isn't designed to store large file and the bandwidth provided is somewhat limited. Below is an imaginary scenario to show you why that's the case:
  > Suppose the repository is part of the materials that some interviewer (especially a domestic one) will go through, he or she will not have the patience to:
  >
  > 1. Go through tons of non-organized files and find some one that looks like a video for "product introduction",
  > 2. Wait for a whole night to download your 432 MB video with poor 100 KB/s speed when downloading your "informative video",
  > 3. Finally click the downloaded file and find that it's broken!

- **Instead, provide some link for your video that supports instant preview and playing**. It's suggested that you upload your video to some public video platform, and to ensure that both domestic/foreign viewers can visit it, you may provide multiple links for different video platform (for the domestic case it's suggested to use [bilibili.com](https://www.bilibili.com/)). If you feel not ready to put it on some public platform, you may share some OneDrive Link. If you've got some video stored in the Zoom account space, you may also choose to share this, but remember to change the storage option for this video as "permanent".
- **For the slides submission, no matter you use the `.pptx` format file or not, you will need to provide a `.pdf` file**. If you insert some animation or video inside your powerpoint file, please remove them or replace them with some picture. As mentioned above, a file with `.pptx` suffix can not be previewed on GitHub, and your interviewer might not have the patience to download it and have a glance of that.
- For the video and the slides mentioned above, explicitly create a hyper link in the [README.md](README.md) for any of your repo viewer to quickly visit the video and the slides.

## Project Report

### Report Organization

We are glad to tell you that for any team that attend the presentation (in the current condition, it means to submit a presentation video), the **Course Project Report** here actually **refers to the [README.md](README.md) on your GitHub repo profile and the other supportive files**. Hence, we are actually checking the quality of your repo, but not some formalistic long report. Your repository is expected to have higher marks if it does:

- Be well organized and looks tidy, without unnecessary files like:
  - Auto-generated cache file and intermediately compiled files
  - Non-common setting files (but shared settings allowed)
  - Large files that can not be previewed (e.g. `.docx` files)
- Give explanation for the repository structure (may use an independent paragraph in the profile and/or in each sub-directories, or describe it in some section like *Program Design*)
- Provide brief and explicit explanation and hyper link for any important and descriptive file (e.g. your TODO list).

Most of the groups have wrote terse and clear project abstract. While for the remaining contents of your report (mainly in the "readme" profile), you may:

- Merge your former **Progress Report** and turned the section to be **Historical Progress**
- Organize and **integrate the contents in your presentation** and turn your presentation manuscript (if any) to be the following sections (to be plugin the report between the abstract and the historical progress):
  - Program Design
  - Functionality Implementation
  - Difficulty Encountered & Solutions (Optional)
- Add **a paragraph about the actual contribution** (not the originally designed one) of each teammate. May add one-sentence personal sentiment in this table by each member.

Note that this is some suggested report structural organization, and you might utilize other organization of writing, but to cover the similar contents.

### Report Submission

We've mentioned that your submission of the video and the report is actually simple, as we are to use your materials on GitHub. However, we urge that you should do the following things:

1. Add an Open Source License in your GitHub repo;
2. Submit a plain text submission with your GitHub repo link on [Blackboard](https://bb.cuhk.edu.cn/) (for every team member each team).

For the first point, it's for protect your authorship but allow others to use your codes. To add a license to your repository, you may check [this](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository). To know the difference of different license, you may check [this](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) provided by GitHub, or directly go to [wiki](https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses). It's recommended to use the [MIT](https://opensource.org/licenses/MIT) license if make it useable in almost every case, while [LGPL-3.0](https://opensource.org/licenses/LGPL-3.0) is recommended if you want to avoid some undesirable revision.

For the second point, it's for any potential case that the external review suddenly requires us to provide more information, and such a submission on BB would be enough to show the strong link between your repo and your BB account.
