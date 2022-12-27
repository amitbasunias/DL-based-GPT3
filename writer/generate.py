import openai

OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

def blog (usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a detailed, very long blog article using the following details. Make sure to add conclusion: \r\n Title: {} \n Keywords: {}\r\n{} Blog article: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer
def blogPost (usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate Title, Introduction, Table of Contents, Continue to expand each Table of Contains into 5 to 10 paragraphs using the following details:\r\n Topic: {} \n Focused keywords: {}\r\n{} Title: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def raffelHeadlines (usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 Raffle Headlines using these details: \r\n Product or Brand: {} \n About: {}\r\n{} 5 Raffle Headlines: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer
def quizHeadlines (usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 Quiz Headlines using these details:\r\n Product or Brand:  {} \n About: {}\r\n{} 5 Quiz Headlines: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def clickbaitHeadlines (usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= "List 5 Clickbait Headlines using these details: \r\n Product or Brand: {} \n About: {}\r\n{} 5 Clickbait Headlines: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer
def newsletterHeadlines (usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 Newsletter Headlines using these details: \r\n Product or Brand:  {} \n About: {}\r\n{} 5 Newsletter Headlines: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def rouineSets(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="What is the {} sets routine for my goal: \r\n Goal: {} \r\n Set 1:" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def obituaryGenerator(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a very detailed, long obituary article using these details:\r\n {} \r\n Obituary article:" .format(usertext, usertone),
        temperature= mustcreativity,
        max_tokens=700,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def gigAbout(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a Tagline about a Fiverr seller using these skills. {} Make sure to write it in 4 Words: \r\n seller name: {} \n Skills: {}" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=10,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def gigResponse(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a response to my Fiverr buyer based on this review. Make sure to finish it in 20 words and use I instead of we:\r\n Review: {u} \r\nMy response:\r\n" .format(usertext),
        temperature= mustcreativity,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def gigStory(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a seller story about a Fiverr seller using these skills. \r\n Skills: {u}" .format(usertext),
        temperature= mustcreativity,
        max_tokens=700,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def gigTags(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Fiverr gig only supports 2 word Meta Keywords: Extract 5 Meta Keywords from this Fiverr Gig and Keywords in upper case separated by a comma: \r\n Fiverr Gig: I will {} .\r\n Keywords: {}\r\n 5 Meta Keywords:\r\n" .format(usertile,usertext, usertone),
        temperature= mustcreativity,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def gigDesc(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write detailed description about My Fiverr Gig using these details \r\n My Fiverr Gig: I will {} \r\n Keywords: {} \r\n tone: {}" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def yttitleGenerator(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List five eye-catching video titles for YouTube videos using the following details:\r\n Channel: {} \r\n About:{} \r\n {}" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def ytchannelDecs(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List five eye-catching video titles for YouTube videos using the following details: \r\n Channel: {} \r\n About: {} \r\n {}" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def ytvideoDesc(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a description for YouTube video using the following details: \r\n Title: {} \r\n Keywords:{} \r\n {} " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def ytvideoScript(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a detailed, very long YouTube Video Script using these details:\r\nProduct or Brand: {} \r\n About: {} \r\n {}" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def cancellationEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a subject for 'Cancellation Email' using these details and then write a 'Cancellation Email' using these details: \r\n Brand: {} \r\n About: {} \r\n {} Subject:" .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def discountEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a subject for 'Coupon or Discount Email' using these details and then write a 'Coupon or Discount Email' using these details \r\n Brand: {} \r\n About:{} \r\n {} Subject: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def followupEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a subject for 'Coupon or Discount Email' using these details and then write a 'Coupon or Discount Email' using these details \r\n Brand: {} \r\n About:{} \r\n {} Subject: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def confirmationEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a subject for 'Confirmation Email' using these details and then write a 'Confirmation Email' using these details: \r\n Brand: {} \r\n About:{} \r\n {} Subject: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def thankyouEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a subject for 'thankyouEmail' using these details and then write a 'thankyouEmail' using these details: \r\n Brand: {} \r\n About:{} \r\n {} Subject: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def welcomeEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a subject for 'welcomeEmail' using these details and then write a 'welcomeEmail' using these details: \r\n Brand: {} \r\n About:{} \r\n {} Subject: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def valueProposition(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a statement that clearly identifies the value proposition of a brand, product, or service to its clients using the following details: \r\n Brand: {} \r\n About:{} \r\n {} Subject: " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def phLaunch(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a product description to launch on the Product Hunt website using the following details: \r\n product: {} \r\n About:{} \r\n {} " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def sloganGenerator(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a very short brand slogan for this brand using these details: \r\n brand: {} \r\n About:{} \r\n {} " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def brandMission(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a very short brand mission for this brand using these details: \r\n brand: {} \r\n About:{} \r\n {} " .format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def brandName(usertext, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a brand name for this: {} \r\n " .format( usertext),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def emailCopy(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write Email Subject and a Marketing Email to a customer using these details: Product:{} \r\n About: {}\r\n {} " .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def productCopy(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a sales copy to a customer for this product: \r\n Product:{} \r\n About: {}\r\n {} " .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def metaKeyword(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Extract meta keywords from this content in lower case separated by a comma: \r\n Content:{} \r\n Meta keywords: {}\r\n " .format( usertile, usertext),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def metaDescription(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a meta description using the following details: \r\n Content:{} \r\n Meta keywords: {}\r\n " .format( usertile, usertext),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def testimonial(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a detailed testimonial about this Product/Website/Service using the following details:\r\n Product/Website/Service: {} \r\n About:{}\r\n {}" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def microCopy(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a microcopy about this Product/Website/Service using the following details:\r\n Product/Website/Service: {} \r\n About:{}\r\n {}" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def microCopy(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a microcopy about this Product/Website/Service using the following details:\r\n Product/Website/Service: {} \r\n About:{}\r\n {}" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def cta(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a call to action for this Product/Website/Service using the following details:\r\n Product/Website/Service: {} \r\n About:{}\r\n {}" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def liadCopy(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a LinkedIn Ad Copy along with the Call To Action for this brand, product, or service using these details:\r\n Brand, Product, or Service: {} \r\n About:{}\r\n {} \r\n LinkedIn Ad Copy:" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def fbprrimaryText(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a Facebook Primary Text along with the Call To Action for this brand, product, or service using these details:\r\n Brand, Product, or Service: {} \r\n About:{}\r\n {} \r\n Facebook Primary Text:" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def adHeadline(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a headline for the Ad copy for this brand, product, or service using these details:\r\n Brand, Product, or Service: {} \r\n About:{}\r\n {}" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def googleDesc(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write an ad description along with the Call To Action for this brand, product, or service using these details. Must be finished within 158 characters:\r\n Brand, Product, or Service: {} \r\n About:{}\r\n {} \r\n Ad description:" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def generaladCopy(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write an ad copy along with the Call To Action for this brand, product, or service using these details:\r\n Brand, Product, or Service: {} \r\n About:{}\r\n {} \r\n Ad Copy:" .format( usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def paraphraser(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Paraphrase this content:\r\n Content: {} \r\n Paraphrase:" .format( usertext),
        temperature= mustcreativity,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def paraphraser(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Paraphrase this content:\r\n Content: {} \r\n Paraphrase:" .format( usertext),
        temperature= mustcreativity,
        max_tokens=3300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def activeVoice(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Convert passive voice into active voice:\r\n Passive Voice: {} \r\n Active Voice:" .format( usertext),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def grammarCorrection(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Correct this to standard English: \r\n {} " .format( usertext),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def productResponse(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a response based on this customer review: \r\n Customer Review: {} \r\n {} Response:" .format( usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def microPr(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a customer review about this product:\r\n Product: {} \r\n {} Customer Review:" .format( usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def productBenefits(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 benefits of this product:\r\n {} " .format(usertext),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def productBpoints(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 very short bullet points for this product:\r\n  Product:{} \r\n".format(usertext),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def productTitle(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 3 product titles based on this product: {} \r\n".format(usertext),
        temperature= mustcreativity,
        max_tokens=3200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def longPr(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a detailed, very long Product Review using the following details. Make sure to add conclusion:\r\n Title: {} \r\n Keywords: {} \r\n {} Blog article:".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def productDesc(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 bullet points for the following product: \r\n Product: {} \r\n ".format(usertext),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def blogPara(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Paraphrase sentence:\r\n sentence: {} \r\n Paraphrase:".format(usertext),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def blogConclusion(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write an in conclusion section for this blog article:\r\n Blog article: {} \r\n {} In Conclusion:".format(usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def blogSection(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write some paragraphs for this blog outline:\r\n Blog Outline: {} \r\n {} Paragraphs:".format(usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def blogOutline(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write 10 outlines for this blog article:\r\n Blog article: {} \r\n 10 outlines:".format(usertext),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def blogIntro(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write an introduction from this blog article:\r\n Blog article: {} \r\n Introduction:".format(usertext),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def blogTitle(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 3 catchy blog titles for this blog article:\r\n Blog article: {} \r\n 3 catchy blog titles:".format(usertext),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer


def newsletterIdeas(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 Newsletter Ideas using these details:\r\nProduct or Brand: {} \r\n About: {}\r\n {} 5 Newsletter Ideas:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer



def newsletterBody(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a detailed, very long Newsletter Body along with the Call to Action using these details: \r\n Product or Brand: {} \r\n About: {}\r\n {}  Newsletter Body:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer




def pptSlides(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate long Slides for PowerPoint for business using these details: \r\n Product or Brand: {} \r\n About: {}\r\n {} Slides for PowerPoint:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def brainstormingIdeas(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate 5 Brainstorming Ideas combining  {} and {} \r\n {} 5 Brainstorming Ideas:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def suveryQuestions(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 10 Survey Questions using these details: \r\n Product or Brand: {} \r\n About: {} \r\n {} 10 Survey Questions:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer


def interviewQuestions(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 10 Interview Questions using these details: \r\n Product or Brand: {} \r\n About: {} \r\n {} 10 Interview Questions:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def classifiedAds(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a Classified Ad along with the Call-To-Action using these details: \r\n Product or Brand: {} \r\n About: {} \r\n {} Classified Ad:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer


def shortCta(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 calls to action for this Product using the these details: \r\n Product: {} \r\n Description: {} \r\n {} 5 calls to action:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer


def coldCalling(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write a detailed cold call phone script along with thank you closing to business owners using these details: \r\n Product or Brand:{} \r\n About: {} \r\n {} Cold call phone script along with thank you closing:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def clickbaitEmail(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="List 5 Clickbait Headlines using these details: \r\n Product or Brand:{} \r\n About: {} \r\n {} 5 Clickbait Headlines:\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer


def emailSeries(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write me:{} \r\n follow-up email series for my new product: \r\n  Product :{} {}\r\n".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def smsMessages(usertile, usertext, usertone, creatives):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Write 7 follow up SMS series using these details: \r\n Product or Brand: {} \r\n About: {} {}\r\n 7 follow up SMS series:".format(usertile, usertext, usertone),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

def microchoiceAnswer(usertile, usertext, tone, creatives, qa, aa, qb, num):
    mustcreativity = "{}" .format(creatives)
    mustcreativity = float(mustcreativity)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate {num} multiple-choice questions and answers based on my target audience and question:\r\n Target Audience: {u} \r\n Question: {qa}\r\n Sample questions:\r\n {aa}\r\n {qb} \r\n {num} multiple-choice questions answers:\r\n".format(u=usertile, ut=usertext, t=tone, c=creatives, qa=qa, aa=aa, qb=qb, num=num),
        temperature= mustcreativity,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices'])>0:
            answer= response['choices'][0]['text']
        else:
            answer = None
    else:
        answer = None
    return answer

