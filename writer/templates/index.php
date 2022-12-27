<?php
//Restrict access
require ("admin/class_password.php"); $protect->enable('user');
//Create new document
if(isset($_POST['addfile'])){
    $filename = $_POST['filename'];
	$addfile = fopen('assets/doc/doc-'.$filename.'<br>'.date('Y-m-d').'<br>'.time().'.php', "w");
}
//Delete document
if (isset($_GET['delp'])) {
    $dird = $_GET['delp'];
    unlink("assets/doc/".$dird);
}
?>
<!DOCTYPE html>
<html class="no-js" lang="en">	
<head>	
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<meta name="description" content="Writing tool powered with OpenAI GPT-3">
	<title>BgWriter</title>
	<link href="assets/css/fontawesome.min.css" rel="stylesheet">
    <link href="assets/css/quill.snow.css" rel="stylesheet">
	<link href="assets/css/app.css" rel="stylesheet">
</head>
<body>
<div id="main" class="main-hidden">
<div class="menu" id="menu">
 <!-- Website name and logout button -->
 <h1>BgWriter<span class="primary">.</span>ai</h1>
 <!-- ::START:: View all documents button -->
 <ul class="nav-list docbtn">
  <li id="documents">
   <i class="fa-solid fa-layer-group"></i>
   <span>Documents</span>
  </li>
 </ul><!-- ::END:: View all documents button -->
 <div class="nav-wrap">
  <div class="accordion">
   <!-- ::START:: Headlines -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-newspaper"></i>
     <span>Headlines Generator (3)</span>
	</div>
    <ul class="nav-list">
	 <li id="raffel-headlines" class="on">
         <span>Raffle Headlines</span>
     </li>
     <li id="quiz-headlines">
         <span>Quiz Headlines</span>
     </li>
     <li id="clickbait-headlines">
         <span>Clickbait Headlines</span>
     </li>
	</ul>
   </div><!-- ::END:: Headlines -->
   <!-- ::START:: Blog Tools -->
   <div class="accordion-box">
    <div class="usecases main-tools">
	 <i class="fa-brands fa-blogger-b"></i>
     <span>Blog Tools (8)</span>
	</div>
    <ul class="nav-list">
	 <li id="blog-post">
         <span>Blog Post</span>
     </li>
     <li id="blog">
         <span>Micro Blog Post</span>
     </li>
     <li id="blog-title">
         <span>Blog Title</span>
     </li>
     <li id="blog-intro">
         <span>Blog Intro</span>
     </li>
     <li id="blog-outline">
         <span>Blog Outline</span>
     </li>
     <li id="blog-section">
         <span>Blog Paragraph</span>
     </li>
     <li id="blog-conclusion">
         <span>Blog Conclusion</span>
     </li>
     <li id="blog-paraphrase">
         <span>Sentence Rewriter</span>
     </li>
	 </ul>
   </div><!-- ::END:: Blog Tools -->
   <!-- ::START:: Product Tools -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-cart-shopping"></i>
     <span>Product Tools (7)</span>
    </div>
    <ul class="nav-list">
     <li id="product-desc">
         <span>Product Description</span>
     </li>
     <li id="long-pr">
         <span>Product Review</span>
     </li>
     <li id="product-title">
         <span>Product Titles</span>
     </li>
     <li id="product-bulletpoints">
         <span>Product Bullet Points</span>
     </li>
     <li id="product-benefits">
         <span>Product Benefits</span>
     </li>
     <li id="micro-pr">
         <span>Micro Product Review</span>
     </li>
     <li id="product-response">
         <span>Review Response</span>
     </li>
	</ul>
   </div><!-- ::END:: Product Tools -->
   <!-- ::START:: Writing Tools -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-square-pen"></i>
     <span>Writing Tools (3)</span>
	</div>
    <ul class="nav-list">
	 <li id="grammar-correction">
         <span>Grammar Correction</span>
     </li>
     <li id="active-voice">
         <span>Passive To Active Voice</span>
     </li>
     <li id="paraphraser">
         <span>Paraphraser</span>
     </li>
	</ul>
   </div><!-- ::END:: Writing Tools -->
   <!-- ::START:: Digital Ad Copy -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-rectangle-ad"></i>
     <span>Digital Ad Copy (6)</span>
	</div>
    <ul class="nav-list">
	 <li id="generalad-copy">
         <span>General Ad Copy</span>
     </li>
     <li id="ad-headline">
         <span>Ad Headlines</span>
     </li>
     <li id="google-desc">
         <span>Google Descriptions</span>
     </li>
     <li id="fbprimary-text">
         <span>Facebook Primary Text</span>
     </li>
     <li id="liad-copy">
         <span>LinkedIn Ad Copy</span>
     </li>
     <li id="classified-ads">
         <span>Classified Ads</span>
     </li>
	</ul>
   </div><!-- ::END:: Digital Ad Copy -->
   <!-- ::START:: Website copy -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-globe"></i>
     <span>Website copy (6)</span>
	</div>
    <ul class="nav-list">
     <li id="short-cta">
         <span>Call To Action(short)</span>
     </li>
     <li id="cta">
         <span>Call To Action</span>
     </li>
     <li id="microcopy">
         <span>Microcopy</span>
     </li>
     <li id="testimonial">
         <span>Testimonial</span>
     </li>
     <li id="meta-description">
         <span>Meta Description</span>
     </li>
     <li id="meta-keyword">
         <span>Meta Keywords</span>
     </li>
     <li id="child-explain">
         <span>Explain to a child</span>
     </li>
	</ul>
   </div><!-- ::END:: Website copy -->
   <!-- ::START:: Sales copy -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-filter-circle-dollar"></i>
     <span>Sales copy (2)</span>
	</div>
    <ul class="nav-list">
	 <li id="product-copy">
         <span>Product sales copy</span>
     </li>
     <li id="email-copy">
         <span>Email sales copy</span>
     </li>
	</ul>
   </div><!-- ::END:: Sales copy -->
   <!-- ::START:: Startup Tools -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-ticket"></i>
     <span>Startup Tools (7)</span>
	</div>
    <ul class="nav-list">
	 <li id="brand-name">
         <span>Brand Name</span>
     </li>
     <li id="brand-mission">
         <span>Brand Mission</span>
     </li>
     <li id="slogan-generator">
         <span>Slogan Generator</span>
     </li>
     <li id="value-proposition">
         <span>Value Proposition</span>
     </li>
     <li id="ph-launch">
         <span>Product Hunt launch</span>
     </li>
     <li id="ppt-slides">
         <span>PowerPoint Slides</span>
     </li>
     <li id="brainstorming-ideas">
         <span>Brainstorming Ideas</span>
     </li>
	</ul>
   </div><!-- ::END:: Startup Tools -->
   <!-- ::START:: Sales Email -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-envelope-circle-check"></i>
     <span>Email copy (10)</span>
	</div>
    <ul class="nav-list">
	 <li id="welcome-email">
         <span>Welcome Email</span>
     </li>
	 <li id="thankyou-email">
         <span>Thank You Email</span>
     </li>
     <li id="confirmation-email">
         <span>Confirmation Email</span>
     </li>
     <li id="followup-email">
         <span>Follow Up Email</span>
     </li>
     <li id="discount-email">
         <span>Coupon/Discount Email</span>
     </li>
     <li id="cancellation-email">
         <span>Cancellation Email</span>
     </li>
     <li id="cold-calling">
         <span>Cold Calling Script</span>
     </li>
     <li id="clickbait-email">
         <span>Clickbait (Outreach email)</span>
     </li>
     <li id="email-series">
         <span>Email series</span>
     </li>
     <li id="sms-messages">
         <span>SMS Messages</span>
     </li>
	</ul>
   </div><!-- ::END:: Sales Email -->
   <!-- ::START:: Newsletter -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-envelope-open-text"></i>
     <span>Newsletter (3)</span>
	</div>
    <ul class="nav-list">
     <li id="newsletter-headlines">
         <span>Newsletter Headlines</span>
     </li>
     <li id="newsletter-ideas">
         <span>Newsletter Ideas</span>
     </li>
     <li id="newsletter-body">
         <span>Newsletter Body</span>
     </li>
	</ul>
   </div><!-- ::END:: Newsletter -->
   <!-- ::START:: Video -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-video"></i>
     <span>Video (4)</span>
	</div>
    <ul class="nav-list">
	 <li id="ytvideo-script">
         <span>YouTube Video Script</span>
     </li>
	 <li id="ytvideo-desc">
         <span>YouTube Video Description</span>
     </li>
     <li id="ytchannel-decs">
         <span>YouTube Channel Description</span>
     </li>
     <li id="yttitle-generator">
         <span>YouTube Title Generator</span>
     </li>
	</ul>
   </div><!-- ::END:: Sales copy -->
   <!-- ::START:: Q&A -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-circle-question"></i>
     <span>Q&A (3)</span>
	</div>
    <ul class="nav-list">
     <li id="survey-questions">
         <span>Survey Questions</span>
     </li>
     <li id="interview-questions">
         <span>Interview Questions</span>
     </li>
     <li id="multichoice-answers">
         <span>Multiple Choice Answers</span>
     </li>
	</ul>
   </div><!-- ::END:: Q&A -->
   <!-- ::START:: Fiverr Gig Tools -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-bars-progress"></i>
     <span>Gig Tools (5)</span>
	</div>
    <ul class="nav-list">	
     <li id="gig-desc">
         <span>Gig Description</span>
     </li>
     <li id="gig-tags">
         <span>Search tags</span>
     </li>
     <li id="gig-response">
         <span>Review Response</span>
     </li>
     <li id="gig-story">
         <span>Short Seller Story</span>
     </li>
     <li id="gig-about">
         <span>About the Seller</span>
     </li>
	</ul>
   </div><!-- ::END:: Fiverr Gig Tools -->
   <!-- ::START:: Miscellaneous -->
   <div class="accordion-box">
    <div class="usecases main-tools">
     <i class="fa-solid fa-boxes-stacked"></i>
     <span>Miscellaneous (3)</span>
	</div>
    <ul class="nav-list">
	 <li id="song-lyrics">
         <span>Song Lyrics</span>
     </li>
     <li id="obituary-generator">
         <span>Obituary Generator</span>
     </li>
     <li id="routine-sets">
         <span>Workout Routine</span>
     </li>
	</ul>
   </div><!-- ::END:: Miscellaneous -->
  </div>
 </div>
</div>
 <div class="page-content">
 <div id="title-wrap">
	<h1 id="title">Raffle Headlines</h1>
</div>

<form id="form" method="post" action="assets/ai/raffel-headlines.php" enctype="multipart/form-data" target="framesource">
<div class="prompt-wrap" id="prompt-title">
<h2 id="opt-heading">Enter product/brand name</h2>	
<textarea id="usertitle" type="text" name="usertitle" placeholder="e.g. BgWriter" spellcheck="false" autocomplete="off"></textarea>
<p class="charlimit" id="titlelimit"></p>
</div>
<h2 id="subheading">Describe your product/brand</h2>	
<div id="main-prompt" class="prompt-wrap">
<textarea id="userprompt" type="text" name="userprompt" placeholder="e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves. With BgWriter, simply input what you need written and our AI technology will take care of the rest, quickly and accurately churning out perfectly written copy every time." spellcheck="false" autocomplete="off"></textarea>
<p class="charlimit" id="keywordlimit"></p>
</div>
<div id="qna-inputs">
<label for="q1">Enter Main Question</label>
<input id="q1" type="text" name="qa" placeholder="e.g. Should I run ads on facebook for my business?">
<label for="a1">Enter Sample Question #1</label>
<input id="a1" type="text" name="aa" placeholder="e.g. Do you pay for advertising now?">
<label for="q2">Enter Sample Question #2</label>
<input id="q2" type="text" name="qb" placeholder="e.g. Do you have a facebook acccount?">
<label for="a2" class="app-input">Enter Answer #2</label>
<input id="a2" type="text" class="app-input" name="ab" placeholder="e.g. If yes, continue to step 3. If no, continue to step 2">
<label for="num">Number of Questions to generate</label>
<input id="num" type="text" name="num" placeholder="e.g. 10">
</div>
<input id="tone" class="app-input" type="text" name="tone" value="">
<input id="template" class="app-input" type="text" name="template" value="0">
<input id="language" class="app-input" type="text" name="language" value="0">
<input id="creativity" class="app-input" type="text" name="creativity" value="7">
<div id="creativity-wrapper">
<label for="creativity-slider">Creativity = </label>
<span id="creativity-counter">7</span>
<input id="creativity-slider" type="range" min="1" max="10" step="1" value="7">
</div>
<div id="tools-wrapper">
<div id="template-wrap">
  <label for="template-option">Framework</label>
  <select id="template-option">
      <option value="0" selected>🚫 Default</option>
      <option value="1">🔵 AIDA</option>
      <option value="2">🟡 PAS</option>
      <option value="3">🟢 BAB</option>
      <option value="4">⚫️ AIDCA</option>
      <option value="5">🟣 PAPA</option>
      <option value="6">⚪️ AIDPPC</option>
      <option value="7">🟤 AICPBSAWN</option>
  </select>
</div>
<div id="tone-wrap">
  <label for="tone-option">Choose a tone</label>
  <select id="tone-option">
    <option selected>🚫 None</option>
    <option value="1">Formal</option>
    <option value="2">Informal</option>
    <option value="3">Optimistic</option>
    <option value="4">Creative</option>
    <option value="5">Friendly</option>
    <option value="6">Professional</option>
    <option value="7">Bold</option>
    <option value="8">Adventurous</option>
    <option value="9">Witty</option>
    <option value="10">Persuasive</option>
    <option value="11">Empathetic</option>
    <option value="12">Conversational</option>
    <option value="13">Questioning</option>
    <option value="14">Assertive</option>
    <option value="15">Directive</option>
    <option value="16">Factual</option>
    <option value="17">Respectful</option>
    <option value="18">Motivating</option>
    <option value="19">Informative</option>
    <option value="20">Flirting</option>
    <option value="21">Sexy</option>
    <option value="22">Loving</option>
    <option value="23">Romantic</option>
    <option value="24">Excited</option>
    <option value="25">Urgent</option>
    <option value="26">Anxious</option>
    <option value="27">Apologetic</option>
    <option value="28">Appreciative</option>
    <option value="29">Bored</option>
    <option value="30">Calm</option>
    <option value="31">Candid</option>
    <option value="32">Cheerful</option>
    <option value="33">Cold</option>
    <option value="34">Concerned</option>
    <option value="35">Courteous</option>
    <option value="36">Critical</option>
    <option value="37">Cruel</option>
    <option value="38">Curious</option>
    <option value="39">Cynical</option>
    <option value="40">Defensive</option>
    <option value="41">Depressed</option>
    <option value="42">Desperate</option>
    <option value="43">Determined</option>
    <option value="44">Diplomatic</option>
    <option value="45">Disappointed</option>
    <option value="46">Disgusted</option>
    <option value="47">Dramatic</option>
    <option value="48">Dreamy</option>
    <option value="49">Eccentric</option>
    <option value="50">Eloquent</option>
    <option value="51">Encouraging</option>
    <option value="52">Enthusiastic</option>
    <option value="53">Excited</option>
    <option value="54">Fearful</option>
    <option value="55">Frustrated</option>
    <option value="56">Funny</option>
    <option value="57">Gloomy</option>
    <option value="58">Happy</option>
    <option value="59">Hesitant</option>
    <option value="60">Hopeful</option>
    <option value="61">Horrific</option>
    <option value="62">Humorous</option>
    <option value="63">Imaginative</option>
    <option value="64">Inspirational</option>
    <option value="65">Judgmental</option>
    <option value="66">Mocking</option>
    <option value="67">Negative</option>
    <option value="68">Nervous</option>
    <option value="69">Patient</option>
    <option value="70">Poetic</option>
    <option value="71">Proud</option>
    <option value="72">Regretful</option>
    <option value="73">Remorseful</option>
    <option value="74">Sarcastic</option>
    <option value="75">Serious</option>
    <option value="76">Snobbish</option>
    <option value="77">Stubborn</option>
    <option value="78">Surprised</option>
    <option value="79">Thankful</option>
    <option value="80">Upset</option>
    <option value="81">Sales</option>
  </select>
</div>
<div id="language-wrap">
  <label for="language-option">Output language</label>
  <select id="language-option">
    <option selected>English</option>
  </select>
</div>
</div>
<input id="submit" class="submit" type="submit" name="submit" value="Create">
</form>

<div id="output" contenteditable="true" spellcheck="false" autocomplete="off"><div class="generating-text"></div></div>
<iframe id="framesource" class="app-input" name="framesource"></iframe>
<div id="save-content-wrap">
<form id="sdoc" method="post" action="assets/php/sdoc.php" enctype="multipart/form-data" target="saveframe">
 <textarea id="savetext" type="text" name="savetext"></textarea>
 <input id="uniquefile" type="text" name="uniquefile" value="">
 <input id="save-btn" type="submit" name="save" value="Save">
</form>
<iframe id="saveframe" class="app-input" name="saveframe"></iframe>
</div>

  <div id="footer">Copyright © <span id="latest-year">2022</span> by BgWriter All Rights Reserved.</div>
 </div>
</div>

<div class="sidebar open" id="sidebar">
  <!-- Create toolbar container -->
<div id="toolbar">
</div>
<div id="editor"></div>
<div id="word-counter">
<span id="saving-text"><i class="fas fa-circle-notch fa-spin"></i> Saving</span>
<!-- Highlighted text options -->
<div id="textoptions">
 <form id="rewriteform" method="post" action="assets/ai/rewrite.php" enctype="multipart/form-data" target="rewritetextframe">
  <textarea id="rewritetext" type="text" name="rewritetext"></textarea>
  <input id="rewrite" type="submit" name="rewrite" value="Rewrite">
 </form>
 <form id="continueform" method="post" action="assets/ai/continue.php" enctype="multipart/form-data" target="continuetextframe">
  <textarea id="continuetext" type="text" name="continuetext"></textarea>
  <input id="continue" type="submit" name="continue" value="Continue">
 </form>
<span id="updating-text"><i class="fas fa-circle-notch fa-spin"></i> Updating</span>
<iframe id="rewritetextframe" class="app-input" name="rewritetextframe"></iframe>
<iframe id="continuetextframe" class="app-input" name="continuetextframe"></iframe>
</div>
<p>Words: <span id="words"></span></p>
</div>
</div>

<div id="files-wrap">
<div id="dashboard">
<h1>BgWriter<span class="primary">.</span>ai</h1>
<div id="dash-menu">
 <ul class="nav-list">
  <li class="all-doc">
   <i class="fa-solid fa-layer-group"></i>
   <span>All Documents</span>
  </li>
 </ul>
 <a href="<?php $protect->createLogout(); ?>" title="Logout"><i class="fa-solid fa-right-from-bracket"></i> Logout</a>
</div>
</div>
 <div id="search-wrap" class="grid">
	<h2>All Documents:</h2>
	<div class="card">
		<p class="primary" id="valid-info">Create a new document</p>
		<form method="post" enctype="multipart/form-data">
			<input type="text" id="filename" name="filename" value="" placeholder="Document" spellcheck="false" autocomplete="off" required>
			<input type="submit" name="addfile" id="addfile" value="New">
		</form>
	</div>
    <?php
	$dirscan = scandir("assets/doc/");
	$srno = 10;
	foreach ($dirscan as $files) {
		if (strpos($files, "doc-") !== false) {
			$simple = explode("doc-", $files);
			$without_extension = basename($simple[1], '.php');
			echo '
	<div class="card">
	<p>'.$without_extension.'</p>  
	<div class="tools">
		<button value="doc-'.$without_extension.'" class="edit-file" title="Edit"><i class="fa-solid fa-pen-nib"></i></button>
		<a href="assets/doc/doc-'.$without_extension.'.php" download="'.$without_extension.'.html" title="Download"><i class="fa-solid fa-download"></i></a>
		<a href="index.php?delp=doc-'.$without_extension.'.php" class="red float-right" title="Delete"><i class="fa fa-trash"></i></a>
		';echo'
	</div>
	</div>';
	$srno++;
		}
	}
	?>
</div>
</div>

<i class="fa-solid fa-bars" id="mob-menu-btn"></i>
<div id="overlay" class="overlay"></div>
<i class="fa-solid fa-pen-to-square" id="open-editor"></i>
<grammarly-button class="grammarly-button"></grammarly-button>

<script src="https://unpkg.com/@grammarly/editor-sdk?clientId=client_EXrxJ6KKpBoAQToMWUUrfw"></script>
<script src="https://kit.fontawesome.com/d128a728e7.js" crossorigin="anonymous"></script>
<script src="assets/js/fontawesome.min.js"></script>
<script src="assets/js/quill.min.js"></script>
<script src="assets/js/app.js"></script>
<script>
</script>
 </body>
</html> 