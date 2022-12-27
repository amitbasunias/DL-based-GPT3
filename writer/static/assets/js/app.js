(function() {
'use strict';
//For iFrame blocking
if (self == top) {
  // Everything checks out, show the page.
  document.documentElement.style.display = 'block';
} else {
  // Break out of the frame.
  top.location = self.location;
}

//For dialog box on closing browser's window
//window.onbeforeunload = () => {return '';};

//For Word Editor
let toolbarOptions = [
  ['undo' , 'redo', { 'header': [1, 2, 3, 4, 5, 6, false] }],
  ['bold', 'italic', 'underline', 'strike'],
  [{'list': 'ordered'}, {'list': 'bullet'}],
  ['link', 'clean'],
];

let icons = Quill.import("ui/icons");
    icons["undo"] = `<svg viewbox="0 0 18 18">
    <polygon class="ql-fill ql-stroke" points="6 10 4 12 2 10 6 10"></polygon>
    <path class="ql-stroke" d="M8.09,13.91A4.6,4.6,0,0,0,9,14,5,5,0,1,0,4,9"></path>
  </svg>`;
    icons["redo"] = `<svg viewbox="0 0 18 18">
    <polygon class="ql-fill ql-stroke" points="12 10 14 12 16 10 12 10"></polygon>
    <path class="ql-stroke" d="M9.91,13.91A4.6,4.6,0,0,1,9,14a5,5,0,1,1,5-5"></path>
  </svg>`;
  
//For Word Counter
Quill.register('modules/counter', function(quill, options) {
  let totalWords = document.getElementById('words');
  quill.on('text-change', function() {
    let quillText = quill.getText();
    totalWords.innerText = quillText.split(/\s+/).length - 1;
  });
});
  
var quillEditor = new Quill('#editor', {
  modules: {
	toolbar: '#toolbar',
    toolbar: toolbarOptions,
    counter: true,
    history: {
      delay: 2000,
      maxStack: 500,
      userOnly: true
    }
  },
  theme: 'snow'
});

//For undo/redo text
document.querySelector(".ql-undo").addEventListener("click", ()=>{
	quillEditor.history.undo();
});
document.querySelector(".ql-redo").addEventListener("click", ()=>{
	quillEditor.history.redo();
});

//For Loading saved file in the editor


//Go to documents

//For saving editer text into files


//Input Filename file


//Basic
let currentYear = document.getElementById("latest-year"),
	formSubmit	= document.getElementById('submit'),
	frameSource = document.getElementById('framesource'),
	outPut = document.getElementById('output'),
	editorBlock = document.querySelector(".ql-editor"),
	sideBar = document.getElementById('sidebar'),
	mainMenu = document.getElementById('menu'),
	bgOverlay = document.getElementById('overlay'),
	mobMenuBtn = document.getElementById("mob-menu-btn"),
	editorBtn = document.getElementById("open-editor");
	
	//For pasting text in contenteditable
	outPut.addEventListener('paste', function (event) {
		event.preventDefault();
		event.stopImmediatePropagation();
		let clearInlineText = event.clipboardData.getData('text/plain');
		document.execCommand('inserttext', false, clearInlineText);
	});

	//For Year
	currentYear.innerHTML = new Date().getUTCFullYear();
	
	//For Mobile nav menubar
	mobMenuBtn.addEventListener("click", ()=>{
		mainMenu.classList.toggle("on");
		bgOverlay.classList.toggle("on");
		mobMenuBtn.classList.toggle("fa-bars");
		mobMenuBtn.classList.toggle("fa-xmark");
		mobMenuBtn.classList.remove("hide");
		editorBtn.classList.toggle("hide");
	});
	
	//For Mobile nav menubar
	editorBtn.addEventListener("click", ()=>{
		sideBar.classList.toggle("on");
		editorBtn.classList.toggle("fa-pen-to-square");
		editorBtn.classList.toggle("fa-xmark");
		mobMenuBtn.classList.toggle("hide");
		editorBtn.classList.remove("hide");
	});
	
	//For main accordion menu list
	let accordion = document.querySelectorAll(".accordion-box");
	accordion.forEach((e)=>{
		e.addEventListener("click", ()=>{
			removeClass();
			e.classList.toggle("active");
			window.scroll({top: 0, left: 0, behavior: 'smooth'});
		});
	});
	function removeClass(){
		accordion.forEach((e)=>{
			e.classList.remove("active");
		});
	}
	
//For blog generators
let raffelHeadlines = document.getElementById("raffel-headlines"),
	quizHeadlines = document.getElementById("quiz-headlines"),
	clickbaitHeadlines = document.getElementById("clickbait-headlines"),
	newsletterHeadlines = document.getElementById("newsletter-headlines"),
	newsletterIdeas = document.getElementById("newsletter-ideas"),
	newsletterBody = document.getElementById("newsletter-body"),
	pptSlides = document.getElementById("ppt-slides"),
	brainstormingIdeas = document.getElementById("brainstorming-ideas"),
	surveyQuestions = document.getElementById("survey-questions"),
	interviewQuestions = document.getElementById("interview-questions"),
	shortCta = document.getElementById("short-cta"),
	clickbaitEmail = document.getElementById("clickbait-email"),
	emailSeries = document.getElementById("email-series"),
	routineSets = document.getElementById("routine-sets"),
	classifiedAds = document.getElementById("classified-ads"),
	coldCalling = document.getElementById("cold-calling"),
	smsMessages = document.getElementById("sms-messages"),
	multichoiceAnswer = document.getElementById("multichoice-answers"),
	blog = document.getElementById("blog"),
	blogPost = document.getElementById("blog-post"),
	blogTitle	= document.getElementById('blog-title'),
	blogIntro = document.getElementById('blog-intro'),
	blogOutline = document.getElementById('blog-outline'),
	blogSection = document.getElementById('blog-section'),
	blogConclusion = document.getElementById('blog-conclusion'),
	blogPara = document.getElementById('blog-paraphrase'),
	productDesc = document.getElementById('product-desc'),
	longPr = document.getElementById('long-pr'),
	productTitle = document.getElementById('product-title'),
	productBpoints = document.getElementById('product-bulletpoints'),
	productBenefits = document.getElementById('product-benefits'),
	microPr = document.getElementById('micro-pr'),
	productResponse = document.getElementById('product-response'),
	grammarCorrection = document.getElementById('grammar-correction'),
	activeVoice = document.getElementById('active-voice'),
	paraphraser = document.getElementById('paraphraser'),
	generaladCopy = document.getElementById('generalad-copy'),
	googleDesc = document.getElementById('google-desc'),
	adHeadline = document.getElementById('ad-headline'),
	fbprimaryText = document.getElementById('fbprimary-text'),
	liadCopy = document.getElementById('liad-copy'),
	cta = document.getElementById('cta'),
	microCopy = document.getElementById('microcopy'),
	testimonial = document.getElementById('testimonial'),
	metaDescription = document.getElementById('meta-description'),
	metaKeyword = document.getElementById('meta-keyword'),
	productCopy = document.getElementById('product-copy'),
	emailCopy = document.getElementById('email-copy'),
	brandName = document.getElementById('brand-name'),
	brandMission = document.getElementById('brand-mission'),
	sloganGenerator = document.getElementById('slogan-generator'),
	valueProposition = document.getElementById('value-proposition'),
	phLaunch = document.getElementById('ph-launch'),
	welcomeEmail = document.getElementById('welcome-email'),
	thankyouEmail = document.getElementById('thankyou-email'),
	confirmationEmail = document.getElementById('confirmation-email'),
	followupEmail = document.getElementById('followup-email'),
	discountEmail = document.getElementById('discount-email'),
	cancellationEmail = document.getElementById('cancellation-email'),
	ytvideoScript = document.getElementById('ytvideo-script'),
	ytvideoDesc = document.getElementById('ytvideo-desc'),
	ytchannelDecs = document.getElementById('ytchannel-decs'),
	yttitleGenerator = document.getElementById('yttitle-generator'),
	gigDesc = document.getElementById('gig-desc'),
	gigTags = document.getElementById('gig-tags'),
	gigResponse = document.getElementById('gig-response'),
	gigStory = document.getElementById('gig-story'),
	gigAbout = document.getElementById('gig-about'),
	songLyrics = document.getElementById('song-lyrics'),
	obituaryGenerator = document.getElementById('obituary-generator'),
	titleText	= document.getElementById('title'),
	subHeading	= document.getElementById('subheading'),
	formAction	= document.getElementById('form'),
	mainPrompt = document.getElementById('main-prompt'),
	qnaInputs = document.getElementById('qna-inputs'),
	promptTitle = document.getElementById('prompt-title'),
	optHeading = document.getElementById('opt-heading'),
	userTitle = document.getElementById('usertitle'),
	userPrompt = document.getElementById('userprompt'),
	toolsWrapper = document.getElementById('tools-wrapper'),
	templateWrap = document.getElementById('template-wrap'),
	templateOption = document.getElementById('template-option'),
	setTemplate = document.getElementById('template'),
	toneWrap = document.getElementById('tone-wrap'),
	toneOption = document.getElementById('tone-option'),
	setTone = document.getElementById('tone'),
	languageWrap = document.getElementById('language-wrap'),
	languageOption = document.getElementById('language-option'),
	setLanguage = document.getElementById('language'),
	keywordLimit =	document.getElementById('keywordlimit'),
	titleLimit = document.getElementById('titlelimit');
	
	//For Raffle Headlines
	raffelHeadlines.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Raffle Headlines";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/raffel-headlines.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		raffelHeadlines.classList.add('on');
	});
	
	//For Quiz Headlines
	quizHeadlines.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Quiz Headlines";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/quiz-headlines.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		quizHeadlines.classList.add('on');
	});
	
	//For Clickbait Headlines
	clickbaitHeadlines.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Clickbait Headlines";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/clickbait-headlines.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		clickbaitHeadlines.classList.add('on');
	});
	
	//For Newsletter Headlines
	newsletterHeadlines.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Newsletter Headlines";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/newsletter-headlines.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		newsletterHeadlines.classList.add('on');
	});
	
	//For Newsletter Ideas
	newsletterIdeas.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Newsletter Ideas";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/newsletter-ideas.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		newsletterIdeas.classList.add('on');
	});
	
	//For Newsletter Body
	newsletterBody.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Newsletter Body";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/newsletter-body.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		newsletterBody.classList.add('on');
	});
	
	//For PowerPoint Slides
	pptSlides.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "PowerPoint Slides";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/ppt-slides.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		pptSlides.classList.add('on');
	});
	
	//For Brainstorming Ideas
	brainstormingIdeas.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Brainstorming Ideas";
		optHeading.innerHTML = "Enter primary product/brand name";
		subHeading.innerHTML = "Enter secondary product, brand name, or any words";
		formAction.action = 'assets/ai/brainstorming-ideas.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. Fitness, Food, Health');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		brainstormingIdeas.classList.add('on');
	});
	
	//For Survey Questions
	surveyQuestions.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Survey Questions";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/survey-questions.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		surveyQuestions.classList.add('on');
	});
	
	//For Interview Questions
	interviewQuestions.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Interview Questions";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/interview-questions.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		interviewQuestions.classList.add('on');
	});
	
	//For Classified Ads
	classifiedAds.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Classified Ads";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/classified-ads.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		classifiedAds.classList.add('on');
	});
	
	//For Short Call to action
	shortCta.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Call to action";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/short-cta.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		shortCta.classList.add('on');
	});
	
	//For Cold Calling Script
	coldCalling.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Cold Calling Script";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/cold-calling.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		coldCalling.classList.add('on');
	});
	
	//For Clickbait (Outreach email)
	clickbaitEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Clickbait (Cold outreach email)";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/clickbait-email.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		clickbaitEmail.classList.add('on');
	});
	
	//For Email series
	emailSeries.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Email series";
		optHeading.innerHTML = "Maxnium no of emails";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/email-series.php';
		userTitle.setAttribute('placeholder', "e.g. 7");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		emailSeries.classList.add('on');
	});
	
	//For SMS Messages
	smsMessages.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "SMS Messages";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/sms-messages.php';
		userTitle.setAttribute('placeholder', "e.g. BgWriter");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		smsMessages.classList.add('on');
	});
	
	//For Multiple Choice Answers
	multichoiceAnswer.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Multiple Choice Answers";
		optHeading.innerHTML = "Target audience:";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/multichoice-answers.php';
		userTitle.setAttribute('placeholder', "e.g. Business owners");
		userPrompt.setAttribute('placeholder', 'e.g. BgWriter is the perfect writing solution for busy business professionals who need high-quality content without the hassle of writing it themselves.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		multichoiceAnswer.classList.add('on');
		qnaInputs.classList.add('on');
		mainPrompt.classList.add('off');
		subHeading.classList.add('off');
	});
	
	//For Long blog
	blogPost.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Blog Post";
		optHeading.innerHTML = "Enter blog title";
		subHeading.innerHTML = "Enter Keywords";
		formAction.action = 'assets/ai/blog-post.php';
		userTitle.setAttribute('placeholder', "e.g. How To Pick A Profitable Blog Niche");
		userPrompt.setAttribute('placeholder', 'e.g. blog, niche, profitable, pick');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		blogPost.classList.add('on');
	});
	
	//For micro blog
	blog.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Micro Blog Post";
		optHeading.innerHTML = "Enter blog title";
		subHeading.innerHTML = "Enter Keywords";
		formAction.action = 'assets/ai/blog.php';
		userTitle.setAttribute('placeholder', "e.g. How To Pick A Profitable Blog Niche");
		userPrompt.setAttribute('placeholder', 'e.g. blog, niche, profitable, pick');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		blog.classList.add('on');
	});
	
	//For blog title
	blogTitle.addEventListener('click', function() {
		titleText.innerHTML = "Blog Title";
		subHeading.innerHTML = "Enter blog topic or Describe blog topic";
		formAction.action = 'assets/ai/blog-title.php';
		userPrompt.setAttribute('placeholder', 'e.g. Google AdSense');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;		
		removemMenuClass();
		toolsWrapper.style.display = "none";
		blogTitle.classList.add('on');
	});
	
	//For blog intro
	blogIntro.addEventListener('click', function() {
		titleText.innerHTML = "Blog Intro";
		subHeading.innerHTML = "Enter blog title or Describe blog topic";
		formAction.action = 'assets/ai/blog-intro.php';
		userPrompt.setAttribute('placeholder', 'e.g. How To Make Money Blogging');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		blogIntro.classList.add('on');
	});
	
	//For blog outline
	blogOutline.addEventListener('click', function() {
		titleText.innerHTML = "Blog Outline";
		subHeading.innerHTML = "Enter blog title or Describe blog topic";
		formAction.action = 'assets/ai/blog-outline.php';
		userPrompt.setAttribute('placeholder', 'e.g. 7 Actionable Steps To Increase Organic Traffic To Your Blog');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		blogOutline.classList.add('on');
	});
	
	//For blog section
	blogSection.addEventListener('click', function() {
		titleText.innerHTML = "Bullet Point to Paragraph";
		subHeading.innerHTML = "Enter bullet point or describe the main point of the paragraph";
		formAction.action = 'assets/ai/blog-section.php';
		userPrompt.setAttribute('placeholder', 'e.g. Writing your first Blog post');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		blogSection.classList.add('on');
	});
	
	//For blog conclusion
	blogConclusion.addEventListener('click', function() {
		titleText.innerHTML = "Blog Conclusion";
		subHeading.innerHTML = "Enter title/bullet points or describe the main point of the blog";
		formAction.action = 'assets/ai/blog-conclusion.php';
		userPrompt.setAttribute('placeholder', 'e.g. How To Build Internal Links for SEO in WordPress');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		blogConclusion.classList.add('on');
	});
	
	//For blog Paraphraser
	blogPara.addEventListener('click', function() {
		titleText.innerHTML = "Sentence Rewriter";
		subHeading.innerHTML = "Enter a sentence.";
		formAction.action = 'assets/ai/blog-paraphrase.php';
		userPrompt.setAttribute("placeholder", "e.g. OpenAI's GPT-3 is a deep learning model that produces human-like text.");
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		blogPara.classList.add('on');
	});
	
	//For Product Descriptions
	productDesc.addEventListener('click', function() {
		titleText.innerHTML = "Product Description";
		optHeading.innerHTML = "Enter Product Name";
		subHeading.innerHTML = "Enter the product title from eCommerce websites like Amazon or describe the product";
		formAction.action = 'assets/ai/product-description.php';
		userTitle.setAttribute('placeholder', "e.g. Techmo");
		userPrompt.setAttribute('placeholder', 'e.g. Lightweight, blue color, highly durable gaming joystick');
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		templateWrap.style.display = "block";
		toneWrap.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		removemMenuClass();
		toneWrap.classList.add('tone-wrap-alt');
		languageWrap.classList.add('language-wrap-only');
		languageWrap.classList.add('pt-20');
		productDesc.classList.add('on');
	});
	
	//For Product Review	
	longPr.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Product Review";
		optHeading.innerHTML = "Enter product name";
		subHeading.innerHTML = "Describe your product";
		formAction.action = 'assets/ai/long-pr.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		longPr.classList.add('on');
	});
	
	//For Product title
	productTitle.addEventListener('click', function() {
		titleText.innerHTML = "Product Titles";
		subHeading.innerHTML = "Enter the product name or describe the product using some keywords.";
		formAction.action = 'assets/ai/product-title.php';
		userPrompt.setAttribute('placeholder', 'e.g. Personalized Doll, Portrait Doll, Amigurumi Doll, Look aLike Doll, Crochet Doll, Gift For Her, Personalized Gift, Gift for Him');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		productTitle.classList.add('on');
	});
	
	//For Product Bullet Points
	productBpoints.addEventListener('click', function() {
		titleText.innerHTML = "Product Bullet Points";
		subHeading.innerHTML = "Enter the product name or describe the product.";
		formAction.action = 'assets/ai/product-bulletpoints.php';
		userPrompt.setAttribute('placeholder', 'e.g. CBD Oil');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		productBpoints.classList.add('on');
	});
	
	//For Product Benefits
	productBenefits.addEventListener('click', function() {
		titleText.innerHTML = "Product Benefits";
		subHeading.innerHTML = "Enter the product name or describe the product using some keywords.";
		formAction.action = 'assets/ai/product-benefit.php';
		userPrompt.setAttribute('placeholder', 'e.g. CBD Oil');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		productBenefits.classList.add('on');
	});
	
	//For Product Review
	microPr.addEventListener('click', function() {
		titleText.innerHTML = "Product Review for a Seller";
		subHeading.innerHTML = "Enter the product name or describe the product using some keywords.";
		formAction.action = 'assets/ai/micro-pr.php';
		userPrompt.setAttribute('placeholder', 'e.g. CBD Oil');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		microPr.classList.add('on');
	});
	
	//For Product Review Response
	productResponse.addEventListener('click', function() {
		titleText.innerHTML = "Review Response";
		subHeading.innerHTML = "Enter customer review.";
		formAction.action = 'assets/ai/product-response.php';
		userPrompt.setAttribute('placeholder', 'e.g. Received the clutch on time, it is beautiful and looks exactly as pictured.');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		productResponse.classList.add('on');
	});
	
	//For Grammar Correction
	grammarCorrection.addEventListener('click', function() {
		titleText.innerHTML = "Grammar Correction";
		subHeading.innerHTML = "Enter a sentence.";
		formAction.action = 'assets/ai/grammar-correction.php';
		userPrompt.setAttribute("placeholder", "e.g. She no went to the market.");
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		grammarCorrection.classList.add('on');
	});
	
	//For Passive To Active Voice
	activeVoice.addEventListener('click', function() {
		titleText.innerHTML = "Passive To Active Voice";
		subHeading.innerHTML = "Enter a sentence.";
		formAction.action = 'assets/ai/active-voice.php';
		userPrompt.setAttribute("placeholder", "e.g. Two trees have been planted by me.");
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		activeVoice.classList.add('on');
	});
	
	//For Paraphraser
	paraphraser.addEventListener('click', function() {
		titleText.innerHTML = "Paraphraser";
		subHeading.innerHTML = "Enter a sentence.";
		formAction.action = 'assets/ai/paraphraser.php';
		userPrompt.setAttribute("placeholder", "e.g. My first trip abroad will always be remembered by me.");
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		paraphraser.classList.add('on');
	});
	
	//For General Ad Copy
	generaladCopy.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "General Ad Copy";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/brand";
		formAction.action = 'assets/ai/generalad-copy.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		generaladCopy.classList.add('on');
	});
	
	//For Google Descriptions
	googleDesc.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Google Descriptions";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/brand";
		formAction.action = 'assets/ai/google-desc.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		googleDesc.classList.add('on');
	});
	
	//For Ad Headlines
	adHeadline.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Ad Headlines";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/brand";
		formAction.action = 'assets/ai/ad-headline.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		adHeadline.classList.add('on');
	});
	
	//For Facebook Primary Text
	fbprimaryText.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Facebook Primary Text";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/brand";
		formAction.action = 'assets/ai/fbprimary-text.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		fbprimaryText.classList.add('on');
	});
	
	//For LinkedIn Ad Copy
	liadCopy.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "LinkedIn Ad Copy";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/brand";
		formAction.action = 'assets/ai/liad-copy.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		liadCopy.classList.add('on');
	});
	
	//For Call To Action
	cta.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Call To Action";
		optHeading.innerHTML = "Enter product/website name";
		subHeading.innerHTML = "Describe your product/website";
		formAction.action = 'assets/ai/cta.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		cta.classList.add('on');
	});
	
	//For Microcopy
	microCopy.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Microcopy";
		optHeading.innerHTML = "Enter product/website name";
		subHeading.innerHTML = "Describe your product/website";
		formAction.action = 'assets/ai/micro-copy.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', `e.g.
About: AI writer that generates content instantly
Features: - Uses language AI and copywriting formulas to generate content
- Simple and easy to use with minimal complexity
- Fast, affordable, and works well on mobile devices`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		microCopy.classList.add('on');
	});
	
	//For Testimonial
	testimonial.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Testimonial";
		optHeading.innerHTML = "Enter product/website name";
		subHeading.innerHTML = "Describe your product/website";
		formAction.action = 'assets/ai/testimonial.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		testimonial.classList.add('on');
	});
	
	//For Meta Descriptions
	metaDescription.addEventListener('click', function() {
		titleText.innerHTML = "Meta Description";
		subHeading.innerHTML = "Enter title or describe the main point of your website";
		formAction.action = 'assets/ai/meta-description.php';
		userPrompt.setAttribute('placeholder', 'e.g. Why & How To Increase Your Website’s Domain Authority');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		metaDescription.classList.add('on');
	});
	
	//For Meta Keywords
	metaKeyword.addEventListener('click', function() {
		titleText.innerHTML = "Meta Keywords";
		subHeading.innerHTML = "Describe the main points of your website";
		formAction.action = 'assets/ai/meta-keywords.php';
		userPrompt.setAttribute('placeholder', 'e.g. 10 Best Keyword Research Tools For SEO');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		metaKeyword.classList.add('on');
	});
	
	//For Product Sales Copy
	productCopy.addEventListener('click', function() {
		titleText.innerHTML = "Product Sales Copy";
		optHeading.innerHTML = "Enter Product/Brand Name";
		subHeading.innerHTML = "Describe your product";
		formAction.action = 'assets/ai/product-copy.php';
		userTitle.setAttribute('placeholder', "e.g. Techmo");
		userPrompt.setAttribute('placeholder', 'e.g. Lightweight, blue color, highly durable gaming joystick');
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		templateWrap.style.display = "block";
		toneWrap.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		removemMenuClass();
		toneWrap.classList.add('tone-wrap-alt');
		languageWrap.classList.add('language-wrap-only');
		languageWrap.classList.add('pt-20');
		productCopy.classList.add('on');
	});
	
	//For Product Sales Copy
	emailCopy.addEventListener('click', function() {
		titleText.innerHTML = "Email Sales Copy";
		optHeading.innerHTML = "Enter Product/Brand Name";
		subHeading.innerHTML = "Describe your product";
		formAction.action = 'assets/ai/email-copy.php';
		userTitle.setAttribute('placeholder', "e.g. Techmo");
		userPrompt.setAttribute('placeholder', 'e.g. Lightweight, blue color, highly durable gaming joystick');
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		templateWrap.style.display = "block";
		toneWrap.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		removemMenuClass();
		toneWrap.classList.add('tone-wrap-alt');
		languageWrap.classList.add('language-wrap-only');
		languageWrap.classList.add('pt-20');
		emailCopy.classList.add('on');
	});
	
	//For Brand Name
	brandName.addEventListener('click', function() {
		titleText.innerHTML = "Brand Name";
		subHeading.innerHTML = "Describe your brand";
		formAction.action = 'assets/ai/brand-name.php';
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		brandName.classList.add('on');
	});
	
	//For Brand Mission
	brandMission.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Brand Mission";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/brand-mission.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		brandMission.classList.add('on');
	});
	
	//For Slogan Generator
	sloganGenerator.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Slogan Generator";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/slogan-generator.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		sloganGenerator.classList.add('on');
	});
	
	//For Value Proposition
	valueProposition.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Value Proposition";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/value-proposition.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		valueProposition.classList.add('on');
	});
	
	//For Product Hunt launch
	phLaunch.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Product Hunt launch";
		optHeading.innerHTML = "Enter product";
		subHeading.innerHTML = "Describe your product";
		formAction.action = 'assets/ai/ph-launch.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', 'e.g. An AI writing tool for auto-generating content and copies for blogs, social media, and more');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		phLaunch.classList.add('on');
	});
	
	//For Welcome Email
	welcomeEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Welcome Email";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/Enter Keypoints";
		formAction.action = 'assets/ai/welcome-email.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', `e.g.
I’d like to personally thank you for signing up to our service
Please reply to this email
Please reach out if any questions
Have a great day!`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		welcomeEmail.classList.add('on');
	});
	
	//For Thank You Note
	thankyouEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Thank You Email";
		optHeading.innerHTML = "Who is the message for?";
		subHeading.innerHTML = "What would you like to thank them for?";
		formAction.action = 'assets/ai/thankyou-email.php';
		userTitle.setAttribute('placeholder', "e.g. John, my cofounder");
		userPrompt.setAttribute('placeholder', 'e.g. Joining me on this startup journey');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		thankyouEmail.classList.add('on');
	});
	
	//For Confirmation Email
	confirmationEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Confirmation Email";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/Enter Keypoints";
		formAction.action = 'assets/ai/confirmation-email.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', `e.g.
We appreciate your purchase! 
Welcome! Let’s get you started
Please reach out if any questions
Have a great day!`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		confirmationEmail.classList.add('on');
	});
	
	//For Follow Up Email
	followupEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Follow Up Email";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/Enter Keypoints";
		formAction.action = 'assets/ai/followup-email.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', `e.g.
In response to your inquiry
Thank you for reaching out to us
Looking forward to hearing from you!`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		followupEmail.classList.add('on');
	});
	
	//For Coupon/Discount Email
	discountEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Coupon/Discount Email";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/Enter Keypoints";
		formAction.action = 'assets/ai/discount-email.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', `e.g.
We have something special for you!
Save 30% off of your next order
Just use this coupon code 33M1EE3
Limited time offer!`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		discountEmail.classList.add('on');
	});
	
	//For Cancellation Email
	cancellationEmail.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "Cancellation Email";
		optHeading.innerHTML = "Enter product/brand name";
		subHeading.innerHTML = "Describe your product/Enter Keypoints";
		formAction.action = 'assets/ai/cancellation-email.php';
		userTitle.setAttribute('placeholder', "e.g. TccnoTrack");
		userPrompt.setAttribute('placeholder', `e.g.
We're sorry to see you go
Confirm your cancellation request`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		cancellationEmail.classList.add('on');
	});
	
	//For YouTube Video Script
	ytvideoScript.addEventListener('click', function() {
		titleText.innerHTML = "YouTube Video Script";
		optHeading.innerHTML = "Enter Product/Brand Name";
		subHeading.innerHTML = "Describe your brand/product";
		formAction.action = 'assets/ai/ytvideo-script.php';
		userTitle.setAttribute('placeholder', "e.g. Marino Insurance Group");
		userPrompt.setAttribute('placeholder', 'e.g. Marino Insurance Group now offers a life insurance policy that can help pay off your home or make your mortgage payments if you pass away. Plus, if you outlive the coverage, you can receive your money back');
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		templateWrap.style.display = "block";
		toneWrap.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		removemMenuClass();
		toneWrap.classList.add('tone-wrap-alt');
		languageWrap.classList.add('language-wrap-only');
		languageWrap.classList.add('pt-20');
		ytvideoScript.classList.add('on');
	});
	
	//For YouTube Video Description
	ytvideoDesc.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "YouTube Video Description";
		optHeading.innerHTML = "Enter video title";
		subHeading.innerHTML = "Enter Keywords/Description";
		formAction.action = 'assets/ai/ytvideo-desc.php';
		userTitle.setAttribute('placeholder', "e.g. SEO for Beginners: Rank #1 In Google");
		userPrompt.setAttribute('placeholder', 'e.g. Search Engine Optimization, Rank your website');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		ytvideoDesc.classList.add('on');
	});
	
	//For YouTube Channel Description
	ytchannelDecs.addEventListener('click', function() {
		promptTitle.style.display = "block";
		titleText.innerHTML = "YouTube Channel Description";
		optHeading.innerHTML = "Enter channel name";
		subHeading.innerHTML = "Enter description";
		formAction.action = 'assets/ai/ytchannel-desc.php';
		userTitle.setAttribute('placeholder', "e.g. OctoKing");
		userPrompt.setAttribute('placeholder', 'e.g. We list viral short videos from around the world.');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		ytchannelDecs.classList.add('on');
	});
	
	//For YouTube Title Generator
	yttitleGenerator.addEventListener('click', function() {
		titleText.innerHTML = "YouTube Title Generator";
		subHeading.innerHTML = "Enter video topic or Describe video topic";
		formAction.action = 'assets/ai/yttitle-generator.php';
		userPrompt.setAttribute('placeholder', 'e.g. a video about the Google AdSense');
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;		
		removemMenuClass();
		toolsWrapper.style.display = "none";
		yttitleGenerator.classList.add('on');
	});
	
	//For Gig Descriptions
	gigDesc.addEventListener('click', function() {
		titleText.innerHTML = "Gig Description";
		optHeading.innerHTML = "Enter gig title";
		subHeading.innerHTML = "Enter Keywords";
		formAction.action = 'assets/ai/gig-description.php';
		userTitle.value = "";
		userTitle.setAttribute('placeholder', "I will do something I'm really good at");
		userPrompt.setAttribute('placeholder', "e.g. on-page optimization, grow your traffic, SEO analysis, primary keyword");
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "block";
		toneWrap.style.display = "block";
		removemMenuClass();
		toneWrap.classList.add('tone-wrap-alt');
		languageWrap.classList.add('language-wrap-only');
		gigDesc.classList.add('on');
	});
	
	//For Gig tags
	gigTags.addEventListener('click', function() {
		titleText.innerHTML = "Search tags";
		optHeading.innerHTML = "Enter gig title";
		subHeading.innerHTML = "Enter keywords or describe gig";
		formAction.action = 'assets/ai/gig-tag.php';
		userPrompt.setAttribute('placeholder', 'e.g. on-page optimization, grow your traffic, SEO analysis, primary keyword');		
		userTitle.value = "";
		userTitle.setAttribute('placeholder', "I will do something I'm really good at");
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		gigTags.classList.add('on');
	});
	
	//For Seller Story
	gigStory.addEventListener('click', function() {
		titleText.innerHTML = "Seller story in one line";
		subHeading.innerHTML = "Enter Skills";
		formAction.action = 'assets/ai/gig-story.php';
		userPrompt.setAttribute('placeholder', 'e.g. Financial research, Financial analysis, Financial planning, Financial reporting, Business plans, Financial projection');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		gigStory.classList.add('on');
	});
	
	//For Gig Review Response
	gigResponse.addEventListener('click', function() {
		titleText.innerHTML = "Review Response";
		subHeading.innerHTML = "Enter buyer review.";
		formAction.action = 'assets/ai/gig-response.php';
		userPrompt.setAttribute('placeholder', 'e.g. Great seller. Very helpful and easy to communicate. Highly recommended.');
		outPut.style.display = "none";
		promptTitle.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		gigResponse.classList.add('on');
	});
	
	//For Gig about
	gigAbout.addEventListener('click', function() {
		titleText.innerHTML = "About The Seller";
		optHeading.innerHTML = "Enter Seller Name(Optional)";
		subHeading.innerHTML = "Enter Skills";
		formAction.action = 'assets/ai/gig-about.php';
		userPrompt.setAttribute('placeholder', 'e.g. 5+ years experiences, video editing, HD quality videos');		
		userTitle.value = "";
		userTitle.setAttribute('placeholder', "e.g. Birju Gurung");
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		templateWrap.style.display = "none";
		toneWrap.style.display = "block";
		removemMenuClass();
		gigAbout.classList.add('on');
	});
	
	//For Song Lyrics
	songLyrics.addEventListener('click', function() {
		titleText.innerHTML = "Song Lyrics";
		subHeading.innerHTML = "Enter song ideas";
		formAction.action = 'assets/ai/song-lyrics.php';
		userPrompt.setAttribute('placeholder', `e.g.
Genre: song genre
Topic: topic or themes of the song
Additional instructions: `);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		songLyrics.classList.add('on');
	});
	
	//For Obituary Generator
	obituaryGenerator.addEventListener('click', function() {
		titleText.innerHTML = "Obituary Generator";
		subHeading.innerHTML = "Enter song ideas";
		formAction.action = 'assets/ai/obituary.php';
		userPrompt.setAttribute('placeholder', `e.g.
First Name: John
Last Name: Smith
Mother: Andrea Smith
Father: Ronald Smith
Birth City: Austin
Birth State: Texas
Date of Birth: 06-23-1991
Date of Death: 9-21-2022
Age At Death: 31
City of Residence: Boise
State Of Residence: Idaho
Academic Degree: Bachelor's of Journalism
Academic Institution: Boise State University
Academic Graduation Date: 9-21-2012
Surviving Kin: Molly Smith, Jacob Smith, Kevin Smith, William Smith
Last Known Occupation: Industrial Welder
Last Known Employer: American Welding Co
Career Field(s): mining, software development, welding
Hobbies: Golf, Skiing, Painting
Achievements: 33rd Degree Mason with the Grand Lodge of Idaho
Special Trait: known for teaching his grandkids how to ride bicycles
Funeral Service Date: 9-23-2022
Funeral Service Venue: Sacred Heart Catholic Church
Funeral Service Venue Address: 333 Main St., Boise, ID 83702
Contact Person: molly@gmail.com`);
		outPut.style.display = "none";
		formSubmit.setAttribute('value', "Create");
		promptTitle.style.display = "none";
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		obituaryGenerator.classList.add('on');
	});
	
	//For Routine sets
	routineSets.addEventListener('click', function() {
		titleText.innerHTML = "Workout Routine";
		optHeading.innerHTML = "Routine for";
		subHeading.innerHTML = "Enter your goal";
		formAction.action = 'assets/ai/routine-sets.php';
		userPrompt.setAttribute('placeholder', 'e.g. workout');		
		userTitle.value = "";
		userTitle.setAttribute('placeholder', "e.g. Lose Weight Fast");
		outPut.style.display = "none";
		promptTitle.style.display = "block";
		formSubmit.setAttribute('value', "Create");
		setTone.setAttribute('value', "");
		toneOption.selectedIndex = 0;
		removemMenuClass();
		toolsWrapper.style.display = "none";
		routineSets.classList.add('on');
	});
	
	//Removes classes from menu	
	function removemMenuClass() {
		surveyQuestions.classList.remove('on');
		ytvideoScript.classList.remove('on');
		raffelHeadlines.classList.remove('on');
		quizHeadlines.classList.remove('on');
		clickbaitHeadlines.classList.remove('on');
		newsletterHeadlines.classList.remove('on');
		newsletterIdeas.classList.remove('on');
		newsletterBody.classList.remove('on');
		pptSlides.classList.remove('on');
		brainstormingIdeas.classList.remove('on');
		interviewQuestions.classList.remove('on');
		classifiedAds.classList.remove('on');
		shortCta.classList.remove('on');
		clickbaitEmail.classList.remove('on');
		emailSeries.classList.remove('on');
		routineSets.classList.remove('on');
		coldCalling.classList.remove('on');
		smsMessages.classList.remove('on');
		multichoiceAnswer.classList.remove('on');
		blog.classList.remove('on');
		blogPost.classList.remove('on');
		blogTitle.classList.remove('on');
		blogIntro.classList.remove('on');
		blogOutline.classList.remove('on');
		blogSection.classList.remove('on');
		blogConclusion.classList.remove('on');
		blogPara.classList.remove('on');
		productDesc.classList.remove('on');
		longPr.classList.remove('on');
		productTitle.classList.remove('on');
		productBpoints.classList.remove('on');
		productBenefits.classList.remove('on');
		microPr.classList.remove('on');
		productResponse.classList.remove('on');
		grammarCorrection.classList.remove('on');
		activeVoice.classList.remove('on');
		paraphraser.classList.remove('on');
		generaladCopy.classList.remove('on');
		googleDesc.classList.remove('on');
		adHeadline.classList.remove('on');
		fbprimaryText.classList.remove('on');
		liadCopy.classList.remove('on');
		cta.classList.remove('on');
		microCopy.classList.remove('on');
		testimonial.classList.remove('on');
		metaDescription.classList.remove('on');
		metaKeyword.classList.remove('on');
		productCopy.classList.remove('on');
		emailCopy.classList.remove('on');
		brandName.classList.remove('on');
		brandMission.classList.remove('on');
		sloganGenerator.classList.remove('on');
		valueProposition.classList.remove('on');
		phLaunch.classList.remove('on');
		welcomeEmail.classList.remove('on');
		thankyouEmail.classList.remove('on');
		confirmationEmail.classList.remove('on');
		followupEmail.classList.remove('on');
		discountEmail.classList.remove('on');
		cancellationEmail.classList.remove('on');
		ytvideoDesc.classList.remove('on');
		ytchannelDecs.classList.remove('on');
		yttitleGenerator.classList.remove('on');
		gigDesc.classList.remove('on');
		gigTags.classList.remove('on');
		gigResponse.classList.remove('on');
		gigStory.classList.remove('on');
		gigAbout.classList.remove('on');
		songLyrics.classList.remove('on');
		obituaryGenerator.classList.remove('on');
		mainMenu.classList.remove("on");
		bgOverlay.classList.remove("on");
		mobMenuBtn.classList.remove("fa-xmark");
		mobMenuBtn.classList.add("fa-bars");
		editorBtn.classList.remove("hide");		
		languageWrap.classList.remove('language-wrap-only');
		languageWrap.classList.remove('pt-20');
		toolsWrapper.style.display = "inline-block";
		toneWrap.classList.remove('tone-wrap-alt');
		mainPrompt.classList.remove("off");
		subHeading.classList.remove('off');
		qnaInputs.classList.remove("on");
	}
	
	//For Creativity
	let creativitySlider = document.getElementById("creativity-slider"),
		creativityCounter = document.getElementById("creativity-counter"),
		creativity = document.getElementById("creativity");
	creativitySlider.oninput = function() {
		creativity.setAttribute('value', this.value);
		creativityCounter.innerHTML = this.value;
	}
	
	//For Template option
	templateOption.addEventListener('change', function() {
		setTemplate.setAttribute('value', this.value);
	});
	
	//For Tone option
	toneOption.addEventListener('change', function() {
		setTone.setAttribute('value', this.value);
	});
	
	//For Language option
	languageOption.addEventListener('change', function() {
		setLanguage.setAttribute('value', this.value);
	});
	
	//For title character limit
	userTitle.addEventListener('input', function() {		
		if (userTitle.value.length > 80) {
    		userTitle.value = userTitle.value.slice(0, 80);
		}
		var titleLength = 80 - userTitle.value.length;
		titleLimit.innerHTML = titleLength;
		if (userTitle.value.length > 79) {
			titleLimit.style.color = "red";
		}else{
			titleLimit.style.color = "black";
		}
	});
	
	//For keywords character limit
	userPrompt.addEventListener('input', function() {		
		if (userPrompt.value.length > 1000) {
    		userPrompt.value = userPrompt.value.slice(0, 1000);
		}
		var txtLength = 1000 - userPrompt.value.length;
		keywordLimit.innerHTML = txtLength;
		if (userPrompt.value.length > 999) {
			keywordLimit.style.color = "red";
		}else{
			keywordLimit.style.color = "black";
		}
	});
  
	//For output text
	formSubmit.addEventListener('click', function() {
		outPut.style.display = "block";
		outPut.innerHTML = '<div class="generating-text"></div>';
		formSubmit.value = "Loading...";
		//For RTL language
		if (setLanguage.value == 1) {
    		outPut.setAttribute('dir', 'rtl');
		}else{
			outPut.setAttribute('dir', 'ltr');
		}
		window.scrollTo({ left: 0, top: document.body.scrollHeight, behavior: "smooth" });
		frameSource.addEventListener('load', function(event) {
			let iframeSrc = frameSource;
			let iframeContents = iframeSrc.contentDocument.body.innerHTML;
			outPut.innerHTML = iframeContents;
			formSubmit.value = "Create";
		});
	});	
	
	//For text highlight options
	let updatingText = document.getElementById('updating-text'),
		textOptions = document.getElementById('textoptions');	
	quillEditor.on('selection-change', function(range, oldRange, source) {
		quillEditor.hasFocus();
		if (range) {
			if (range.length == 0) {
				textOptions.classList.remove('on');
			} else {
				var textHighlighted = quillEditor.getText(range.index, range.length);	  
				var rewriteText = document.getElementById('rewritetext'),
					continueText = document.getElementById('continuetext');
					rewriteText.innerText = textHighlighted;
					continueText.innerText = textHighlighted;
					textOptions.classList.add('on');
			}
		} else {
			textOptions.classList.remove('on');
		}
	});
  
	//For text rewriting
	document.getElementById('rewrite').addEventListener('click', function() {
		quillEditor.hasFocus();
		updatingText.classList.add('on');
		document.getElementById('rewritetextframe').addEventListener('load', function(event) {
			let rewriteContents = document.getElementById('rewritetextframe').contentDocument.body.innerHTML;
			let cursorPosition = quillEditor.getSelection(true);
				quillEditor.insertText(cursorPosition, rewriteContents);
				document.execCommand('insertText', false, '');
				updatingText.classList.remove('on');
				textOptions.classList.remove('on');
		});
	});
  
	//For text continue
	document.getElementById('continue').addEventListener('click', function() {
		quillEditor.hasFocus();
		updatingText.classList.add('on');
		document.getElementById('continuetextframe').addEventListener('load', function(event) {
			let continueContents = document.getElementById('continuetextframe').contentDocument.body.innerHTML;
			let cursorText = quillEditor.getSelection(true);
				quillEditor.insertText(cursorText, continueContents);
				document.execCommand('insertText', false, '');
				updatingText.classList.remove('on');
				textOptions.classList.remove('on');
		});
	});	

	//For Grammarly
	Grammarly.init().then((grammarly) => {
	grammarly.addPlugin(quillEditor.root, {
		autocomplete: "on",
		documentDialect: "american"
	});
	});
	
})();