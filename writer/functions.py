from .generate import *
def direction(usertile, usertext, tone, creatives, qa, aa, qb, num):
    if 'micoblog':
        output = blog(usertile, usertext, tone, creatives)
    elif 'raffelHeadlines':

        output = raffelHeadlines(usertile, usertext, tone, creatives)

    elif 'quizHeadlines':

        output = quizHeadlines(usertile, usertext, tone, creatives)

    elif 'clickbaitHeadlines':

        output = clickbaitHeadlines(usertile, usertext, tone, creatives)

    elif 'newsletterHeadlines':

        output = newsletterHeadlines(usertile, usertext, tone, creatives)

    elif 'rouineSets':

        output = rouineSets(usertile, usertext, tone, creatives)

    elif 'obituaryGenerator':

        output = obituaryGenerator(usertile, usertext, tone, creatives)
    elif 'gigAbout':

        output = gigAbout(usertile, usertext, tone, creatives)
    elif 'gigResponse':

        output = gigResponse(usertile, usertext, tone, creatives)

    elif 'gigStory':

        output = gigStory(usertile, usertext, tone, creatives)
    elif 'gigTags':

        output = gigTags(usertile, usertext, tone, creatives)
    elif 'gigDesc':

        output = gigDesc(usertile, usertext, tone, creatives)
    elif 'yttitleGenerator':

        output = yttitleGenerator(usertile, usertext, tone, creatives)
    elif 'ytchannelDecs':

        output = ytchannelDecs(usertile, usertext, tone, creatives)
    elif 'ytvideoDesc':

        output = ytvideoDesc(usertile, usertext, tone, creatives)

    elif 'ytvideoScript':

        output = ytvideoScript(usertile, usertext, tone, creatives)

    elif 'cancellationEmail':

        output = cancellationEmail(usertile, usertext, tone, creatives)

    elif 'discountEmail':

        output = discountEmail(usertile, usertext, tone, creatives)

    elif 'followupEmail':

        output = followupEmail(usertile, usertext, tone, creatives)
    elif 'confirmationEmail':

        output = confirmationEmail(usertile, usertext, tone, creatives)

    elif 'thankyouEmail':

        output = thankyouEmail(usertile, usertext, tone, creatives)
    elif 'welcomeEmail':

        output = welcomeEmail(usertile, usertext, tone, creatives)
    elif 'valueProposition':

        output = valueProposition(usertile, usertext, tone, creatives)
    elif 'phLaunch':

        output = phLaunch(usertile, usertext, tone, creatives)
    elif 'sloganGenerator':

        output = sloganGenerator(usertile, usertext, tone, creatives)

    elif 'brandMission':

        output = brandMission(usertile, usertext, tone, creatives)

    elif 'brandName':

        output = brandName(usertile, usertext, tone, creatives)


    elif 'emailCopy':

        output = emailCopy(usertile, usertext, tone, creatives)

    elif 'productCopy':

        output = productCopy(usertile, usertext, tone, creatives)

    elif 'metaKeyword':

        output = metaKeyword(usertile, usertext, tone, creatives)


    elif 'metaDescription':

        output = metaDescription(usertile, usertext, tone, creatives)


    elif 'testimonial':

        output = testimonial(usertile, usertext, tone, creatives)


    elif 'microCopy':

        output = microCopy(usertile, usertext, tone, creatives)


    elif 'cta':

        output = cta(usertile, usertext, tone, creatives)


    elif 'liadCopy':

        output = liadCopy(usertile, usertext, tone, creatives)


    elif 'fbprrimaryText':

        output = fbprrimaryText(usertile, usertext, tone, creatives)


    elif 'adHeadline':

        output = adHeadline(usertile, usertext, tone, creatives)



    elif 'googleDesc':

        output = googleDesc(usertile, usertext, tone, creatives)


    elif 'generaladCopy':

        output = generaladCopy(usertile, usertext, tone, creatives)


    elif 'paraphraser':

        output = paraphraser(usertile, usertext, tone, creatives)


    elif 'activeVoice':

        output = activeVoice(usertile, usertext, tone, creatives)


    elif 'grammarCorrection':

        output = grammarCorrection(usertile, usertext, tone, creatives)


    elif 'productResponse':

        output = productResponse(usertile, usertext, tone, creatives)


    elif 'microPr':

        output = microPr(usertile, usertext, tone, creatives)


    elif 'productBenefits':

        output = productBenefits(usertile, usertext, tone, creatives)


    elif 'productBpoints':

        output = productBpoints(usertile, usertext, tone, creatives)


    elif 'productTitle':

        output = productTitle(usertile, usertext, tone, creatives)


    elif 'longPr':

        output = longPr(usertile, usertext, tone, creatives)


    elif 'productDesc':

        output = productDesc(usertile, usertext, tone, creatives)


    elif 'blogPara':

        output = blogPara(usertile, usertext, tone, creatives)


    elif 'blogConclusion':

        output = blogConclusion(usertile, usertext, tone, creatives)


    elif 'blogSection':

        output = blogSection(usertile, usertext, tone, creatives)


    elif 'blogOutline':

        output = blogOutline(usertile, usertext, tone, creatives)


    elif 'blogIntro':

        output = blogIntro(usertile, usertext, tone, creatives)


    elif 'blogTitle':

        output = blogTitle(usertile, usertext, tone, creatives)


    elif 'newsletterIdeas':

        output = newsletterIdeas(usertile, usertext, tone, creatives)


    elif 'newsletterBody':

        output = newsletterBody(usertile, usertext, tone, creatives)


    elif 'pptSlides':

        output = pptSlides(usertile, usertext, tone, creatives)


    elif 'brainstormingIdeas':

        output = brainstormingIdeas(usertile, usertext, tone, creatives)


    elif 'suveryQuestions':

        output = suveryQuestions(usertile, usertext, tone, creatives)


    elif 'interviewQuestions':

        output = interviewQuestions(usertile, usertext, tone, creatives)


    elif 'classifiedAds':

        output = classifiedAds(usertile, usertext, tone, creatives)


    elif 'shortCta':

        output = shortCta(usertile, usertext, tone, creatives)


    elif 'coldCalling':

        output = coldCalling(usertile, usertext, tone, creatives)


    elif 'clickbaitEmail':

        output = clickbaitEmail(usertile, usertext, tone, creatives)


    elif 'emailSeries':

        output = emailSeries(usertile, usertext, tone, creatives)


    elif 'smsMessages':

        output = smsMessages(usertile, usertext, tone, creatives)


    elif 'microchoiceAnswer':

        output = microchoiceAnswer(usertile, usertext, tone, creatives, qa, aa, qb, num)


    elif 'blogPost':

        output = blogPost(usertile, usertext, tone, creatives, qa, aa, qb, num)

    return (output)