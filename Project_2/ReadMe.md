### Overview:
<p>This is a hybrid Convolutional-Dense Neural Network project that trains a model capable of distinguishing among images of the Simpson Family members.  The project encompasses downloading data directly from Kaggle, creating the directory structures needed to house the data in a way that can be used by the Neural Network, Preprocessing the Data,Training the Model, and Validating the result.  The takeaway here is that with a little help and study, a novice data scientist is capable of training a reasonably good classification alogorithm.  With a little more practice, a model like this could be used at work to save time and refocus the efforts of team members on my analytical tasks.</p>

### Goals:
<ol>
<li>Gain Experience with Neural Networks</li>
<li>Create a model that classifies Simpson Family Members well</li>
<li>Work in Google Colab</li>
</ol>

### Motivation and Background
<p>The motivation for this project was to try out for myself Convolutional Neural Networks.  I had been watching the Professor do the work in class, and I wanted an opportunity to give it a shot for myself.  The result here is something that performs reasonably well, correctly identifying a simpson family member 80% of the time, when the random probability is 20%.  With some additional work this could be applied in the work setting.</p>

### Notebook Location
<p>Note that both the Final and the Working Colab Notebooks are 11mb, which is too large to share in github.  The below link leads to my google drive.
https://drive.google.com/drive/folders/1YmJveBOd7oDE8n-LROPeSE5vniUZ6UM-?usp=sharing
    
### Data
<ul><li><b>Source:</b>  Kaggle </li>
    <li><b>Hyperlink:</b> https://www.kaggle.com/alexattia/the-simpsons-characters-dataset/download</li>
    <li><b>Author/Reason for Creation:</b> Alex Attia created this dataset "to build a neural network which can recognize characters."</li>
    <li><b>Size:</b>  1.13 GB of images comprising 20 characters from the Simpsons.  Eac character has between 117 and 2,246 images.</li>
    <li><b>Suitability:</b> This was a great dataset.  I had no issues working with it.  Plus it was fun to use the Simpson Characters.</li><\ul>


### Table of Contents

<ol><li>Business Problem</li>
    <li>Data - Images</li>
    <li>Explore/Prepare Data</li>
    <li>Copy the Image Data into the Directory Structure</li>
    <li>Explore/Tune Different Models</li>
    <li>TensorBoard</li>
    <li>Data Augmentation and Final Training</li>
    <li>Final Solution/Validating the Results</li>
    <li>Limitations and Later Work</li>
    <li>References and Contributions</li></ol>

### Software Requirements
<ol>
<li>Kaggle Token</li>
<li>Google Colab - w/GPU access</li>
<li>zipfile</li>
<li>sklearn</li>
<li>keras</li>
<li>tensorflow</li>
<li>tensorboard</li>
<li>numpy</li></ol>
