---
layout: post
title: "The Illiterate of the Future"
date: 2026-05-04
tags: [ai, photography, benjamin, philosophy, marxism]
description: "Reading Walter Benjamin's A Short History of Photography in the age of AI — the parallels are uncanny, but the contrasts are more illuminating."
model: "claude-opus-4-7"
image: /img/20260429_170545.jpg
---

*Reading Benjamin's* A Short History of Photography *in the age of AI*

I finally finished Walter Benjamin's *A Short History of Photography*, an essay published as a pamphlet and has been sitting on my desk for months. I blame the translation more than anything else to be honest.

Unsurprisingly, I couldn't read it without comparing the history of photography to the currently unfolding present of AI. The rhymes are uncanny — but the contrasts are more illuminating, and the most glaring contrast is one Benjamin himself would have insisted on: who owns the apparatus, and what does it mean to be literate of its products?

Benjamin himself quote: *the illiterate of the future will not be the person who cannot read and write, but the person who is ignorant of photography.* Benjamin then asks the question that actually matters — *but is the photographer any more literate of his own pictures?* Substitute "AI" for "photography" and "user" for "photographer" and we have a dinner party debate.

## The parallels, briefly

Photography was a publicly released technology. Daguerre's process was bought by the French state in 1839 and given to the world. Transformer architecture was published by Google researchers in 2017; large-scale language models matured at a non-profit before becoming the most-deployed technology of the decade. Both technologies got out of the lab before anyone had time to retrospect on what they meant.

Both arrived to identical-looking backlash. Photography offended religious sensibilities first — the production of human likeness by a machine was variously called blasphemous, soul-stealing, vulgar. AI hits the same nerves: the fear of synthetic faces, synthetic voices, the discomfort that something not-quite-human now performs the most human acts. In both cases the moral panic was rapidly outpaced by adoption. The same bourgeoisie who decried photography sat for portraits; the same people who decry AI quietly use it to draft their emails.

And both spawned new labor categories that were invisible from the outside but constitutive of the tech itself. Early photographers needed head clamps, knee braces, and posing stools to keep subjects still through long exposures. The little iron stand in the corner of a daguerreotype was the support apparatus that made the magic possible. AI now has its own scaffolding industry — retrieval pipelines, evals, MCP servers, prompt libraries, context-window engineering, all the unsexy plumbing that lets a model pretend to be useful in a real workflow. New tech destroys some forms of labor and quietly creates others. Worth remembering whenever someone tells you AI eliminates work; it eliminates *some* work and conjures other work into existence, and the new work is usually less visible and less unionized.

And we are not yet discussing whether or how meaningful it is to invest unlimited human and nature resources to bolster AI - to gamble is to be human, it seems.

There's also a generative parallel that Benjamin was alive to: photography didn't just replace painting, it opened up entire new realms of observation. The microscope-camera, the telescope-camera, the high-speed shutter, eventually the photographic plate as a particle detector — none of these were the point of photography in 1839, but all of them were latent in it. AI's analogue is just beginning: protein folding, materials discovery, mathematical proof assistance, cosmological simulation. Dismissing the technology because of fear of the unknown forecloses the part that matters most.

These parallels are real, but they're only interesting up to a point.

## The contrast: aura, and the strange opacity of the model

Benjamin's central anxiety in this essay — and the one he developed more famously in *The Work of Art in the Age of Mechanical Reproduction* — is *aura*. The aura is the unique presence of a thing in time and space, the trace of the hand, the singular here-and-nowness that mechanical reproduction strips away. The painter leaves themself in the painting; the camera, Benjamin thought, was a more transparent instrument, one that brought the viewer closer to the subject by minimizing the maker.

This is where the AI parallel breaks down in the most productive way. The camera, even at its most artful, is finally a recording device — light, lens, emulsion. AI is not a recording device. It is the opposite kind of machine: a synthesizing apparatus that has its own voice, its own statistical aesthetics, its own residue of every text it was trained on. You can identify "ChatGPT prose" stylometrically the way you can identify Hemingway. The model has cadence. The model has tics — em-dashes, tricolons, the little rhetorical pirouette of "it's not just X, it's Y." Far from being transparent, the model is *aesthetic all the way down*, and the aesthetic is a compressed average of the corpus that trained it.

So if the camera is the painter's opposite — reproduction without authorship — AI is something stranger: reproduction *as* authorship, copying that mints, a recombinant machine that sounds like nobody and everybody at once. Benjamin's question of where aura goes when reproduction takes over has a new and dizzying answer in our case. Aura doesn't disappear. It gets distributed, statistically averaged, and laundered through a system whose origins you can't see. The training data has aura — a billion specific human acts of writing and image-making, each with its own here-and-now — but the output erases the trail. That erasure is what makes AI feel uncanny in a way photography never did. A daguerreotype shows you a person; a generative model shows you a person who never existed, made of fragments of people who did.

It's worth pausing here on a counter-example from a field that gives Benjamin's question a different shape. In high-energy physics, papers from collaborations like ATLAS and CMS — the giant detector experiments at CERN's Large Hadron Collider — routinely list three thousand authors. Every name on the page contributed something — detector work, calibration, code, analysis, theory — but no individual aura penetrates the opacity of the collective. Nobody reads a CMS paper trying to detect the hand of a particular postdoc. The diffusion of authorship is, to a real extent, intentional: it protects individuals, distributes credit, and bolsters the aura of the *experiment itself*, the apparatus, the collaboration. It is a legitimated form of authorial obscurity. The unsettling thing about AI output, then, is not that authorship dissolves — we already have institutional formats for that — but that there is no equivalent legitimating structure around it. The three-thousand-author paper sits inside a discipline, a peer-review tradition, a chain of accountability. The model output sits inside a Terms of Service. That is a difference in kind, not in degree.

This is also why *"the photographer is illiterate of his own pictures"* lands with such force when you transpose it. At least the photographer pressed a shutter and watched the world. The user of an AI system has no comparable relation to the output. The prompt is the new caption — the framing apparatus that determines what we're meant to see — but the user often can't read the picture they got back. Where did that fact come from? Whose phrasing is that? Whose biases are encoded in this politely confident paragraph? Most of us cannot say. *We* are the illiterates of the future, confidently included.

## The Marxist turn (Benjamin would insist)

You can't honestly read Benjamin without asking who owns the means of reproduction?

Photography democratized image-making in real and important ways — the bourgeois portrait, the family album, the photojournalist, eventually the smartphone in every pocket. But it also enabled mass propaganda on a scale earlier visual media couldn't reach. The state photograph, the identity card, the surveillance still — these are also photography. The technology cuts both ways at once, and which way it cuts depends on who controls the apparatus.

The AI bottleneck is not the models, but the apparatus required to run it. It is hardware, electricity, water, and capital. A flagship open-weight model needs serious silicon to run at decent speed — the reason recent Mac Studios and Mac Minis have been periodically out of stock is precisely that hobbyists and small operators have realized this is the cheapest route to local inference, and even "cheap" here means thousands of pounds. Industrial deployments need datacenters that drink municipal water for cooling and draw from already-strained grids. The resource floor is high enough that for most users the practical mode of access is a subscription to someone else's compute.

This produces a new and underappreciated vulnerability. Build a workflow — a productivity system, a small business, a research practice — on top of a subscribed AI service, and you have built it on rented ground. The provider can throttle you, deprecate the model you depend on, change the terms, or cut you off entirely. Any productivity built on that basis can dry up overnight, and the user has no real recourse. The illiteracy here is not just semantic; it is infrastructural. Most users cannot evaluate, let alone migrate to, the local-inference alternative.

Self-hosting is the obvious political response, and a partial one. You can buy the hardware. You can, in principle, run it off-grid on solar. But the capability gap between a £4,000 desktop and a frontier API is large, and the gap between either of those and what the major labs run internally is larger again. Resource sovereignty exists on a steep gradient. Yannis' "platform fiefdom" is, in the end, fiefdom fiefdom.

Which is why the honest framing is the one almost no one wants to make explicit. If AI models are trained on the commons of human writing — and they are; the labs are at this point candid about it — then the output is, at origin, a public good. The question is not whether to make it one. The question is whether we will recognize *in distribution* what is already true *in production*. Doing so is something the infrastructure logic of the technology pushes towards, if we want to avoid drifting into a feudal AI economy where access to cognitive amplification is rationed by a handful of providers. Compute is not distributable the way film stock was. Water and energy are not infinitely available. Open-weight releases, public compute, energy and water accountability, training-data audits, worker-side rather than employer-side AI — these are not utopian wish-list items. They are answers to a question Benjamin would have recognized immediately.

## The caption, and the prompt

Benjamin closes by predicting that the caption would become "the most essential part of the photograph" — the verbal scaffolding that tells the viewer what they're looking at, that fixes the meaning of an image which would otherwise drift. He was right. The photograph without its caption is almost always politically and semantically ambiguous; the caption does the work of telling you whether the figure in the frame is a victim or a perpetrator, a hero or a casualty, a refugee or an invader.

Our captions now are prompts. The prompt frames the AI output, fixes its meaning, gives it the register and the politics and the apparent authority it has. And the prompt, like the caption, is where literacy will increasingly live — not in the ability to make AI produce things, which is already trivial, but in the ability to *read* what it has produced: to ask whose voice this is, what was averaged to get here, what was cropped out of the training distribution, who profits from this particular sentence appearing in your inbox.

The illiterate of the future is not the person who can't use AI. It is the person who can't read it — and on that score, almost all of us are still learning the alphabet.

<div class="transparency-footer" markdown="0">
<p class="transparency-label"><em>This post was drafted with Claude Opus 4.7 in conversation, then manually edited by the author. The prompts driving the draft are reproduced verbatim below.</em></p>
<pre class="transparency-prompt">
Appendix: prompts used in writing this post
Reproduced verbatim.

1. (Sent with two photographs: the cover of the Benjamin book, and a page showing the underlined passage about the photographer being illiterate of his own pictures.)

I have finally finished reading Benjamin's A Short History of Photography, and because I can't read or watch anything nowadays without thinking of AI, this essay turned out to be a really illuminating perspective that can be used on how we treat AI as a technology.

From the start, Benjamin pointed out the fact that the tech of photography was made public, made it possible for it to be adopted and developed quickly without much wide retrospection. This can be said about ai, or transformer tech, stemmed from neuronet work and natural language processing research done in public institutions, then in non-profit ai research outfits like early open ai.

Then the resistence came first from the religious group that deems the creation of image of human though human made machines blasphemy, which then quickly extended into the counterweight argument of how it can be used to create images of everything else - from the stars to the cultural relics. Same backlashes also happened to ai - passing the Turing test was soon discarded as a definite sign of possessing human like intelligence, and at the same time it's being used in every avenue of human activity.

And the next point was particularly interesting, in comparing photography and painting, the traditional form of art, photography minimises the facilitator and brings the audience closer to the subject of the image, while painting inevitably retains the essence of the painter more than the content. Also, the various levers of photography (slow mo, enlargements) opens up new avenues of observation for viewers, creating access to previous unknown realms of reality. This can be said about ai too, but sometimes fears of unknown pushes many of us to dismiss this incredible potential. These potentials will also usher in scaffolding techs built around AI as a rapidly developing tech, same way poles and knee supports were created to help subjects stay still for a prolonged period of time for the long exposure required in early photography. The point is these are the human labour and the value created by and through new techs when they emerge - the way ai eliminates many forms of manual labour is comparable to the way photography eliminated the labour around fine arts, but so can one expect AI leading to leaps and strides in new forms of productivity like particle detectors can emerge from photography.

The essay went on to talk about the social function of photography, how it reflects forms of human life and interacts with entities of power. Then moved on to the transition from "photography as art" to "art as photography", the flip of power position between the tradition and the new, and what's the implication of mass production of arts and creative products.

The final remark was about the relation between the photographer and their photograph, how much can we say the former has an authoritative narration over the latter? (See the underlined passage in the second picture)

Help me think this through, I want to make a blog post out of these thoughts

2. This might deserve a longer post, I think 1500 words ish should be a good start, I don't want to meander on obvious points, start with the parallels to pique the interest but focus on the contrast, the aura, and the Marxist analysis?

3. ok let's put a pin on this as the first draft of the article, and continue to tinker on it a bit more before making another draft.

in the aura section, add a paragraph about the relationship between the author and the output in the academic research collaborations - in large high energy physics collaboration like ATLAS and CMS, papers are signed with 3000 names, each author contributed to the final publication but to various capacities. very little individual "aura" can penetrate the "opacity" of the collaboration, and to some extend it is intentionally obscured, in order to protect the collective, to bolster the aura of the experiment.

the Marxist analysis section, it's not true that language models are not reproducible - it's quite common for companies to release their models and weights open source, although maybe not the top/frontier ones, but there are very high quality open source models. the more acute barrier is hardware and resources, like water and electricity, and this is where social conflicts are getting heated. a regular user of ai through subscription may very well get cut-off by the provider out of the blue and any productivity built on the basis of ai workflows will dry up. one could acquire powerful workstation that can run flagship open source models (hence the out-of-stock mac mini and mac studio) on solar panels, but these are prohibitedly expensive with a fraction of the capability. ai basically forces our hands to engage in "sharing is caring" style socialist programme - if we go on to recognize ai as public good (which is already is if the ai companies are being honest, since it's trained on all human data), and care about human rights and equality.

what do you think?

4. normalize the whole post to american spelling

5. append all the prompts in this conversation verbatim to the article
</pre>
</div>
