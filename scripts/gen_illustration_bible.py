#!/usr/bin/env python3
# -*- coding: utf-8 -*-

BASE_STYLE = "warm children's picture-book illustration, soft rounded shapes, thick clean linework in deep indigo (#2E2A47), gouache/watercolor digital texture, big expressive eyes, pastel palette (lavender #7B6FC4, coral #E85D42, sunny yellow #F4B93C, sage green #5AA588, soft blue #4E85B8), toddler-book proportions, warm soft lighting, no photorealism, no anime style"

CONSISTENCY = """Maintain exact character consistency across every illustration: same face, hairstyle, proportions and clothing for every recurring character throughout the entire book.
Melina = 5.5-year-old girl, brown bob haircut with soft front fringe, pink bow on the side, big brown eyes, light freckles across the nose, denim overall dungarees over a yellow-and-white striped shirt, pink sneakers.
Biscuit = small cream/white fluffy puppy, floppy brown ears, blue collar.
Mom = brown hair in a ponytail, soft lavender cardigan.
Dad = short curly hair, glasses, plaid shirt.
Grandma = silver hair in a bun, floral-print apron.
Grandpa = white moustache, brimmed hat, plaid vest.
Sofia = curly red hair, girl, same age as Melina.
Nikos = energetic boy, about 6 years old.
Leonidas = quiet boy, about 5 years old, neighbor."""

NEGATIVE = "no photorealism, no anime/manga style, no scary or dark imagery, no text or letters in image, no extra limbs or distorted hands/faces, no adult body proportions, not blurry, no logos or watermarks, no violence, no clinical or medical imagery"

# ============ SCENE ILLUSTRATIONS (26) ============
scenes = [
{"id":"I-001","page":"i","size":"Full page","priority":"HIGH","camera":"Eye level, medium shot","chars":"Μελίνα, Μπισκότο","emotion":"Ζεστασιά, χαρά, οικειότητα",
 "palette":"Dominant: 🟡 yellow · Secondary: 🟣 lavender · Accent: 🩷 coral",
 "desc":"Εξώφυλλο: Η Μελίνα καθισμένη στο χαλί του δωματίου της, αγκαλιά με τον Μπισκότο, γύρω τους ανοιχτά βιβλία και μολύβια, ζεστό απογευματινό φως.",
 "prompt":"Book cover illustration. Melina sitting cross-legged on a rug in her bedroom, hugging Biscuit the puppy, surrounded by open picture books and colored pencils, warm afternoon light through a window, cozy bedroom with a bookshelf and a small plant, joyful and safe atmosphere.",
 "aspect":"3:4","safe":"Keep Melina and Biscuit centered in the lower two-thirds; leave open sky/wall space in the upper third for title text overlay."},
{"id":"I-002","page":"1","size":"Spot illustration","priority":"HIGH","camera":"Wide shot, three-quarter angle","chars":"Μελίνα, Μπισκότο","emotion":"Χαρά",
 "palette":"Dominant: 🟡 yellow · Secondary: 🩷 coral · Accent: 🟢 sage",
 "desc":"Η Μελίνα χοροπηδά με ανοιχτά χέρια μπροστά από έναν ψηλό πύργο τουβλάκια, ο Μπισκότο πηδά χαρούμενος δίπλα της, ζεστό ηλιόλουστο δωμάτιο.",
 "prompt":"Melina jumping joyfully with arms wide open in front of a tall block tower she just built, Biscuit the puppy jumping happily beside her with tongue out, sunny living room, warm golden light, sense of triumphant celebration.",
 "aspect":"4:3","safe":"Keep the tower and both characters within the central safe area; avoid cropping Melina's raised arms at the frame edge."},
{"id":"I-003","page":"8","size":"Spot illustration","priority":"HIGH","camera":"Close-up, eye level","chars":"Μελίνα, Μπισκότο","emotion":"Λύπη",
 "palette":"Dominant: 🔵 soft blue · Secondary: 🟣 lavender · Accent: 🟡 yellow",
 "desc":"Η Μελίνα κάθεται στο πάτωμα με σκυμμένο κεφάλι, κρατώντας ένα σκισμένο ζωγραφισμένο χαρτί με ουράνιο τόξο, ο Μπισκότο ακουμπά το κεφάλι του στο γόνατό της με ένοχο βλέμμα.",
 "prompt":"Melina sitting on the floor with her head down, holding a torn hand-drawn rainbow picture in both hands, small tears, Biscuit the puppy resting his head gently on her knee with a guilty, apologetic expression, soft muted afternoon light, tender and quiet mood.",
 "aspect":"4:3","safe":"Keep the torn paper visible and readable as a rainbow drawing; keep both faces unobscured within central frame."},
{"id":"I-004","page":"11","size":"Half page","priority":"MEDIUM","camera":"Wide shot, eye level","chars":"Μελίνα, Μαμά, Μπισκότο","emotion":"Παρηγοριά, ανακούφιση",
 "palette":"Dominant: 🟣 lavender · Secondary: 🔵 soft blue · Accent: 🟡 yellow",
 "desc":"Η Μελίνα, η μαμά και ο Μπισκότο αγκαλιασμένοι στο πάτωμα δίπλα στα δύο κομμάτια του σκισμένου σχεδίου, ζεστό φως.",
 "prompt":"Melina, her mom, and Biscuit the puppy sitting together on the floor in a gentle group hug, the two torn pieces of the rainbow drawing resting nearby, warm soft lamp light, calm and comforting mood, mom's ponytail and lavender cardigan visible.",
 "aspect":"4:3","safe":"Keep the hug group centered; leave breathing room above heads for the page's question text that sits directly above this image."},
{"id":"I-005","page":"15","size":"Spot illustration","priority":"HIGH","camera":"Eye level, medium shot","chars":"Μελίνα, Νίκος, Μπισκότο","emotion":"Θυμός",
 "palette":"Dominant: 🔴 coral-red · Secondary: 🟡 yellow · Accent: 🟢 sage",
 "desc":"Η Μελίνα στέκεται με σφιγμένες γροθιές και κόκκινα μάγουλα, μπροστά της ο Νίκος κρατά το αρκουδάκι της, ο Μπισκότο κοιτά ανήσυχος.",
 "prompt":"Melina standing with clenched fists and flushed red cheeks, an angry but not scary expression, facing Nikos (energetic 6-year-old boy) who holds her teddy bear, Biscuit the puppy watching anxiously from the side, living room setting, tense but safe family moment.",
 "aspect":"4:3","safe":"Keep both children's faces and the teddy bear clearly visible within the central frame."},
{"id":"I-006","page":"19","size":"Spot illustration","priority":"LOW","camera":"Top-down, wide shot","chars":"Μελίνα, Μπισκότο","emotion":"Παιχνιδιάρικη συγκέντρωση",
 "palette":"Dominant: 🟢 sage · Secondary: 🟣 lavender · Accent: 🟡 yellow",
 "desc":"Η Μελίνα και ο Μπισκότο παίζουν επιτραπέζιο πάνω σε ένα χαλί, ζάρι στη μέση, χαμογελαστοί.",
 "prompt":"Top-down view of Melina and Biscuit the puppy playing a small board game on a living room rug, a die in the middle, both smiling, warm cozy afternoon light.",
 "aspect":"4:3","safe":"Keep the board game board and both characters within frame, slight vignette at edges is fine."},
{"id":"I-007","page":"21","size":"Spot illustration","priority":"HIGH","camera":"Eye level, medium shot","chars":"Μελίνα, Μπαμπάς","emotion":"Φόβος",
 "palette":"Dominant: 🟣 lavender · Secondary: 🔵 soft blue · Accent: 🟡 yellow",
 "desc":"Η Μελίνα στέκεται στην άκρη της πισίνας, κρατώντας σφιχτά το χέρι του μπαμπά, κοιτάζοντας διστακτικά το νερό, δίπλα της τυλιγμένο σε πετσέτα το κουνελάκι Καρότο.",
 "prompt":"Melina standing at the edge of a swimming pool, gripping her dad's hand tightly, looking hesitantly at the blue water, a plush bunny (Carrot) wrapped in a towel beside her on a pool chair, dad kneeling beside her with glasses and a plaid shirt, bright outdoor pool setting, nervous but supported mood.",
 "aspect":"4:3","safe":"Keep the pool edge line roughly at the lower third; keep Melina and dad's joined hands unobscured in the center."},
{"id":"I-008","page":"27","size":"Spot illustration","priority":"MEDIUM","camera":"Wide shot, eye level","chars":"Μελίνα, Σοφία, Νίκος, Λεωνίδας, Μπισκότο","emotion":"Έκπληξη",
 "palette":"Dominant: 🟠 orange · Secondary: 🩷 coral · Accent: 🟡 yellow",
 "desc":"Η Μελίνα με ορθάνοιχτα μάτια και ανοιχτό στόμα, μπροστά της φίλοι κρατούν μια τούρτα με κεράκια, ο Μπισκότο φοράει στραβό καπελάκι πάρτι.",
 "prompt":"Melina with wide-open eyes and an open-mouth surprised expression, facing a small group of friends (a curly-red-haired girl, an energetic boy, a quiet boy) holding up a birthday cake with lit candles, Biscuit the puppy wearing a crooked party hat, colorful balloons in the background, joyful surprise-party mood.",
 "aspect":"4:3","safe":"Keep Melina's surprised face and the cake both within frame; balloons can bleed off the top edge."},
{"id":"I-009","page":"32","size":"Spot illustration","priority":"HIGH","camera":"Eye level, close-up","chars":"Μελίνα, Μπισκότο","emotion":"Ηρεμία",
 "palette":"Dominant: 🟢 sage · Secondary: 🟣 lavender · Accent: 🟡 yellow (lamp glow)",
 "desc":"Η Μελίνα καθισμένη στο κρεβάτι της με μια κουβέρτα, διαβάζει ένα βιβλίο, ο Μπισκότο κοιμάται κουλουριασμένος δίπλα της, απαλό φως βραδινού.",
 "prompt":"Melina sitting on her bed wrapped in a soft blanket, reading a picture book, Biscuit the puppy curled up asleep beside her, warm dim evening lamp light, peaceful bedtime mood, cozy bedroom with a small nightlight.",
 "aspect":"4:3","safe":"Keep the bed and both characters centered; soft vignette toward edges is fine for this calm scene."},
{"id":"I-010","page":"38","size":"Full page","priority":"HIGH","camera":"Wide shot, three-quarter angle","chars":"Μελίνα, Μπισκότο","emotion":"Χαρά (πριν την υπερφόρτωση)",
 "palette":"Dominant: 🟡 yellow · Secondary: 🟢 sage · Accent: 🩷 coral",
 "desc":"Η Μελίνα και ο Μπισκότο τρέχουν χαρούμενοι προς την τσουλήθρα, ζωντανή παιδική χαρά με πολλά παιδιά στο βάθος, ζεστά χρώματα.",
 "prompt":"Melina and Biscuit the puppy running happily toward a slide in a lively, colorful playground, several children playing in the background on swings and a roundabout, bright sunny day, cheerful and energetic mood.",
 "aspect":"3:4","safe":"Keep Melina and Biscuit in sharp focus in the foreground center-left; background children can be looser/smaller."},
{"id":"I-011","page":"39","size":"Half page","priority":"MEDIUM","camera":"Eye level, medium shot","chars":"Μελίνα, Μπισκότο","emotion":"Αισθητηριακή κόπωση",
 "palette":"Dominant: 🟣 lavender · Secondary: 🔵 soft blue · Accent: 🟡 yellow",
 "desc":"Η Μελίνα στέκεται πιο σιωπηλή ανάμεσα σε παιδιά που παίζουν, κοιτάζει γύρω της, ο Μπισκότο δίπλα της με στοργικό βλέμμα.",
 "prompt":"Melina standing very still and quiet among other children playing energetically around her, slightly overwhelmed expression, looking around, Biscuit the puppy pressed gently against her leg looking up with a caring expression, busy playground background slightly blurred to suggest sensory overload, empathetic mood.",
 "aspect":"4:3","safe":"Keep Melina's face clearly readable in the center; background children can be softly blurred toward the edges."},
{"id":"I-012","page":"43","size":"Spot illustration","priority":"LOW","camera":"Wide shot, top-down","chars":"Μελίνα, Μπισκότο","emotion":"Μετάβαση θορύβου→ηρεμίας",
 "palette":"Dominant: 🟣 lavender · Secondary: 🟢 sage · Accent: 🩷 coral",
 "desc":"Μικρή εικόνα της περιστρεφόμενης πλατφόρμας στη μία άκρη και του ήσυχου παγκακιού στην άλλη, σαν αρχή και τέλος διαδρομής.",
 "prompt":"Simple split illustration: a spinning playground roundabout on one side fading into a quiet park bench under a tree on the other side, small path connecting them, symbolic before/after composition, soft colors.",
 "aspect":"4:3","safe":"Keep both landmarks recognizable and roughly equal in visual weight left/right."},
{"id":"I-013","page":"47","size":"Full page","priority":"HIGH","camera":"Eye level, medium shot","chars":"Μελίνα, Μαμά","emotion":"Θυμός",
 "palette":"Dominant: 🔴 coral-red · Secondary: 🔵 soft blue · Accent: 🟡 yellow",
 "desc":"Η Μελίνα μπροστά στην τηλεόραση, με σφιγμένες γροθιές και κόκκινα μάγουλα, η μαμά γονατισμένη δίπλα της με ήρεμο βλέμμα.",
 "prompt":"Melina standing in front of a TV with clenched fists and a flushed, frustrated expression, mom kneeling beside her at eye level with a calm, understanding expression, cozy living room in the evening, warm lamp light, emotionally tense but safe family moment.",
 "aspect":"3:4","safe":"Keep both faces at eye-level within the central band of the frame; TV can be softly out of focus in the background."},
{"id":"I-014","page":"55","size":"Full page","priority":"HIGH","camera":"Wide shot, three-quarter angle","chars":"Μελίνα","emotion":"Λύπη / μοναξιά",
 "palette":"Dominant: 🔵 soft blue · Secondary: 🟢 sage · Accent: 🟡 yellow",
 "desc":"Η Μελίνα κάθεται μόνη σε ένα σκαλοπάτι της αυλής του σχολείου, παρακολουθώντας από μακριά δύο συμμαθήτριές της να παίζουν.",
 "prompt":"Melina sitting alone on a school-yard step, head slightly bowed, watching two classmates play together in the distance, schoolyard with trees and a playground in the background, wistful and quietly sad mood, soft daylight.",
 "aspect":"3:4","safe":"Keep Melina in the foreground lower-third; the playing classmates should read as small and distant in the background."},
{"id":"I-015","page":"63","size":"Full page","priority":"HIGH","camera":"Eye level, medium shot","chars":"Μελίνα, Μπαμπάς","emotion":"Φόβος",
 "palette":"Dominant: 🟣 lavender · Secondary: 🟡 yellow · Accent: 🩷 coral",
 "desc":"Η Μελίνα στέκεται στην πόρτα μιας αίθουσας χορού, κρύβοντας το πρόσωπό της στο πλάι του μπαμπά, βλέποντας από μακριά άλλα παιδιά με ρούχα χορού.",
 "prompt":"Melina standing at the doorway of a dance studio, partially hiding her face against her dad's side, peeking shyly at other children in dance outfits inside the room, dad kneeling with a reassuring hand on her shoulder, bright studio interior with a wall of mirrors, nervous-but-supported mood.",
 "aspect":"3:4","safe":"Keep the doorway framing centered; Melina and dad should occupy the foreground, dance studio visible but softly behind them."},
{"id":"I-016","page":"70","size":"Full page","priority":"HIGH","camera":"Eye level, wide shot","chars":"Μελίνα, Νίκος, Μπαμπάς","emotion":"Απογοήτευση",
 "palette":"Dominant: 🟡 yellow · Secondary: 🔴 coral-red · Accent: 🟢 sage",
 "desc":"Επιτραπέζιο παιχνίδι στο τραπέζι, ο Νίκος πανηγυρίζει επειδή έφτασε πρώτος στο τέρμα, η Μελίνα κοιτάζει τα πιόνια με απογοήτευση.",
 "prompt":"A board game laid out on a table, Nikos cheering with raised arms because his piece reached the finish first, Melina looking at the game pieces with a disappointed pout, dad sitting across the table with a calm supportive expression, cozy living room, bittersweet family game-night mood.",
 "aspect":"3:4","safe":"Keep the game board and all three characters within frame; board details can be simplified/soft-focus."},
{"id":"I-017","page":"74","size":"Spot illustration","priority":"LOW","camera":"Eye level, wide shot","chars":"Μελίνα, Νίκος, Μπαμπάς","emotion":"Χαρούμενη αναμέτρηση","palette":"Dominant: 🟢 sage · Secondary: 🟡 yellow · Accent: 🩷 coral",
 "desc":"Η Μελίνα, ο Νίκος και ο μπαμπάς γύρω από ένα επιτραπέζιο παιχνίδι, χαμογελαστοί, ζάρι στον αέρα.",
 "prompt":"Melina, Nikos and dad sitting around a board game, all smiling, a die caught mid-air as if just thrown, playful family moment, warm living room light.",
 "aspect":"4:3","safe":"Keep all three faces visible; die can be slightly motion-blurred mid-air."},
{"id":"I-018","page":"77","size":"Full page","priority":"MEDIUM","camera":"Wide shot, eye level","chars":"Μελίνα","emotion":"Ανυπομονησία",
 "palette":"Dominant: 🟢 sage · Secondary: 🟡 yellow · Accent: 🩷 coral",
 "desc":"Η Μελίνα στέκεται δίπλα στις κούνιες της παιδικής χαράς, περιμένοντας τη σειρά της, κοιτάζοντας τα λουλούδια στο γρασίδι.",
 "prompt":"Melina standing beside a row of playground swings, waiting her turn with a slightly impatient but curious expression, looking down at colorful flowers in the grass, another child swinging in the background, sunny playground setting, patient waiting mood.",
 "aspect":"3:4","safe":"Keep Melina and the flowers in the lower half of the frame; swings and waiting child can occupy the upper half."},
{"id":"I-019","page":"85","size":"Full page","priority":"MEDIUM","camera":"Eye level, medium shot","chars":"Μελίνα, άγνωστο παιδί, Μαμά","emotion":"Απόρριψη / περιέργεια",
 "palette":"Dominant: 🟡 yellow · Secondary: 🔵 soft blue · Accent: 🟣 lavender",
 "desc":"Η Μελίνα στέκεται μπροστά σε ένα παιδί που παίζει μόνο του με μπάλα, με ερωτηματικό βλέμμα· η μαμά κάπως πιο πίσω παρακολουθεί με στοργή.",
 "prompt":"Melina standing in front of another child who is playing alone with a ball and has just said no to playing together, Melina has a puzzled, slightly hurt expression, mom standing a little further back watching with a warm supportive expression, sunny playground, gentle bittersweet mood.",
 "aspect":"3:4","safe":"Keep Melina's questioning expression and the other child's ball both visible in the central frame."},
{"id":"I-020","page":"93","size":"Full page","priority":"HIGH","camera":"Wide shot, three-quarter, sense of motion","chars":"Μελίνα, Μπαμπάς","emotion":"Αποφασιστικότητα",
 "palette":"Dominant: 🟡 yellow · Secondary: 🟢 sage · Accent: 🔵 soft blue",
 "desc":"Η Μελίνα πάνω στο ποδήλατό της χωρίς βοηθητικές ρόδες, ο μπαμπάς κρατά ελαφρά τη σέλα, και τα δύο χαμογελαστά αλλά συγκεντρωμένα.",
 "prompt":"Melina riding a bicycle without training wheels, dad lightly holding the back of the seat while jogging alongside, both with focused, determined smiles, a sunny neighborhood street with trees, encouraging and hopeful mood, sense of motion.",
 "aspect":"3:4","safe":"Keep the bicycle and both characters in the lower two-thirds; street/trees can extend into the upper third."},
{"id":"I-021","page":"101","size":"Full page","priority":"HIGH","camera":"Eye level, close-up","chars":"Μαμά, Μελίνα, Παππούς","emotion":"Αποχωρισμός",
 "palette":"Dominant: 🟣 lavender · Secondary: 🩷 coral · Accent: 🟡 yellow (warm light)",
 "desc":"Η μαμά φοράει το παλτό της δίπλα στην πόρτα, γονατισμένη στο ύψος της Μελίνας, κρατώντας της ένα μικρό κασκόλ· ο παππούς περιμένει χαμογελαστός από πίσω.",
 "prompt":"Mom kneeling at Melina's eye level by the front door, wearing her coat, handing Melina a small scarf to hold, grandpa (white moustache, hat, plaid vest) waiting warmly in the background, entryway of a cozy home, tender goodbye mood, soft evening light.",
 "aspect":"3:4","safe":"Keep mom and Melina's eye-level exchange centered; grandpa can be softly positioned in the background."},
{"id":"I-022","page":"109","size":"Full page","priority":"HIGH","camera":"Wide shot, eye level","chars":"Μελίνα, παιδιά, Γιαγιά","emotion":"Υπερδιέγερση",
 "palette":"Dominant: 🩷 coral · Secondary: 🟡 yellow · Accent: 🟣 lavender",
 "desc":"Πάρτι γενεθλίων, πολλά παιδιά τραγουδούν δυνατά γύρω από τούρτα με κεράκια, μπαλόνια, η Μελίνα καλύπτει ελαφρά τα αυτιά της.",
 "prompt":"A lively birthday party scene with several children singing loudly around a cake with candles, balloons and streamers, Melina standing slightly apart with her hands gently covering her ears, a slightly overwhelmed expression, grandma visible nearby noticing her, warm indoor party lighting.",
 "aspect":"3:4","safe":"Keep Melina's covered-ears gesture clearly visible in the foreground; the singing group can be busy/dense in the background."},
{"id":"I-023","page":"116","size":"Full page","priority":"MEDIUM","camera":"Eye level, medium shot","chars":"Μελίνα, Μπαμπάς","emotion":"Ανάγκη ησυχίας",
 "palette":"Dominant: 🟢 sage · Secondary: 🟡 yellow · Accent: 🩷 coral",
 "desc":"Η Μελίνα μόλις μπήκε σπίτι με τη σχολική της τσάντα, ο μπαμπάς κρατά ένα παιχνίδι έτοιμος να παίξουν, εκείνη δείχνει απαλά την ήρεμη γωνιά της.",
 "prompt":"Melina just walking in the front door still wearing her school backpack, dad standing nearby holding a board game eagerly, Melina gently pointing toward her cozy reading corner across the room, warm entryway lighting, understanding and patient family mood.",
 "aspect":"3:4","safe":"Keep Melina and dad in the foreground; the calm corner she's pointing to can be softly visible in the background."},
{"id":"I-024","page":"123","size":"Full page","priority":"MEDIUM","camera":"Close-up, eye level","chars":"Μελίνα, Μπισκότο","emotion":"Απογοήτευση / αποφασιστικότητα",
 "palette":"Dominant: 🟡 yellow · Secondary: 🟢 sage · Accent: 🟣 lavender",
 "desc":"Η Μελίνα προσπαθεί να δέσει μόνη της τα κορδόνια της, με μπερδεμένο βλέμμα, ο Μπισκότο κοιτάζει από δίπλα.",
 "prompt":"Melina sitting on the floor trying to tie her own shoelaces, a puzzled and slightly frustrated expression, tangled laces, Biscuit the puppy sitting beside her watching curiously, cozy hallway setting, determined problem-solving mood.",
 "aspect":"3:4","safe":"Keep Melina's hands and the shoelaces clearly visible and readable in the central frame."},
{"id":"I-025","page":"130","size":"Full page","priority":"HIGH","camera":"Eye level, medium shot","chars":"Μελίνα, Μπισκότο","emotion":"Υπερηφάνεια / ολοκλήρωση",
 "palette":"Dominant: 🟣 lavender · Secondary: 🟡 yellow · Accent: 🟢 sage",
 "desc":"Η Μελίνα κάθεται στην ήρεμη γωνιά της με τον Μπισκότο, γύρω τους μικρές φανταστικές φυσαλίδες με όλα τα συναισθήματα του βιβλίου.",
 "prompt":"Melina sitting contentedly in her cozy calm corner with Biscuit the puppy curled beside her, surrounded by small whimsical floating bubble-shapes each containing a different simple emoji-like face (happy, sad, angry, scared, surprised, calm), warm evening light, reflective and proud mood, sense of a completed journey.",
 "aspect":"3:4","safe":"Keep Melina and Biscuit centered; the floating emotion bubbles can be arranged loosely around the upper frame."},
{"id":"I-026","page":"134","size":"Spot illustration","priority":"LOW","camera":"Wide shot, eye level","chars":"Μελίνα, Μαμά, Μπαμπάς, Μπισκότο","emotion":"Γιορτινή ολοκλήρωση",
 "palette":"Dominant: 🟣 lavender · Secondary: 🩷 coral · Accent: 🟡 yellow",
 "desc":"Όλη η οικογένεια γύρω από το μεγάλο επιτραπέζιο, γιορτινή ατμόσφαιρα, μικρές φυσαλίδες συναισθημάτων στον αέρα.",
 "prompt":"The whole family (Melina, mom, dad) and Biscuit the puppy gathered around the large final board game, festive celebratory atmosphere, tiny floating emotion-face bubbles in the air, warm family-game-night lighting.",
 "aspect":"4:3","safe":"Keep all family members within frame; bubbles can float off the top edge."},
]

print(f"Scenes: {len(scenes)}")

# ============ REUSABLE ASSET LIBRARY ============
assets = []

# Biscuit poses (10)
biscuit_poses = [
    ("Χαρούμενο πήδημα", "jumping mid-air with tongue out, ears flapping, pure joy"),
    ("Καθισμένος προσεκτικός", "sitting attentively, head tilted to one side, listening"),
    ("Κοιμισμένος κουλουριασμένος", "curled up asleep in a tight ball, peaceful"),
    ("Ανήσυχος με γερμένο κεφάλι", "standing with head tilted, worried/concerned expression"),
    ("Τρέχει", "running joyfully, ears flying back, motion lines"),
    ("Παρηγορητική παρουσία", "sitting quietly pressed against someone's leg, gentle supportive look"),
    ("Με καπελάκι πάρτι", "wearing a small crooked party hat, festive"),
    ("Σκάβει/κρύβει κάτι", "digging or burying a small object in the ground, playful mischief"),
    ("Ένοχο βλέμμα", "guilty expression, ears down, head lowered slightly"),
    ("Σε εγρήγορση", "sitting upright, ears perked up, alert and curious"),
]
for i, (name, desc) in enumerate(biscuit_poses, start=1):
    assets.append({
        "id": f"A-{i:03d}", "cat": "🐶 Μπισκότο — στάσεις", "name": name,
        "prompt": f"Reference sheet asset: Biscuit the puppy (small cream/white fluffy puppy, floppy brown ears, blue collar), {desc}, plain neutral background, clean isolated character study.",
        "priority": "HIGH" if i <= 4 else "MEDIUM",
    })

n0 = len(biscuit_poses)

# Melina expressions (8)
melina_expr = [
    ("Χαρά", "wide joyful smile, eyes crinkled with happiness"),
    ("Λύπη", "downturned mouth, watery eyes, gentle sadness"),
    ("Θυμός", "furrowed brow, flushed cheeks, clenched jaw, not scary"),
    ("Φόβος", "wide eyes, slightly open mouth, nervous eyebrows"),
    ("Έκπληξη", "wide open eyes and mouth in an 'O' shape"),
    ("Ηρεμία", "soft closed-mouth smile, relaxed eyes, peaceful"),
    ("Αποφασιστικότητα", "determined focused expression, slight smile, tongue-out concentration"),
    ("Σκεπτική/Περίεργη", "head tilted, one eyebrow raised, curious thinking expression"),
]
for i, (name, desc) in enumerate(melina_expr, start=n0+1):
    assets.append({
        "id": f"A-{i:03d}", "cat": "👧 Μελίνα — εκφράσεις προσώπου", "name": name,
        "prompt": f"Reference sheet asset: Melina (5.5-year-old girl, brown bob haircut with front fringe, pink side bow, big brown eyes, light freckles) headshot/bust portrait, expression: {desc}, plain neutral background, clean isolated character study.",
        "priority": "HIGH",
    })

n1 = n0 + len(melina_expr)

# Carrot bunny (1)
assets.append({
    "id": f"A-{n1+1:03d}", "cat": "🥕 Καρότο (λούτρινο)", "name": "Βασική αναφορά",
    "prompt": "Reference sheet asset: Carrot, Melina's small plush bunny toy, soft beige fur, floppy ears, one slightly worn ear, simple friendly stitched-smile face, plain neutral background.",
    "priority": "HIGH",
})
n2 = n1 + 1

# Secondary characters (7)
secondary = [
    ("Μαμά", "Mom: brown hair in a ponytail, soft lavender cardigan, warm gentle smile, full-body reference pose"),
    ("Μπαμπάς", "Dad: short curly hair, glasses, plaid shirt, warm approachable smile, full-body reference pose"),
    ("Γιαγιά", "Grandma: silver hair in a bun, floral-print apron, kind smile, full-body reference pose"),
    ("Παππούς", "Grandpa: white moustache, brimmed hat, plaid vest, cheerful smile, full-body reference pose"),
    ("Σοφία", "Sofia: curly red hair, girl about 5-6 years old, cheerful expression, full-body reference pose"),
    ("Νίκος", "Nikos: energetic boy about 6 years old, short brown hair, big grin, full-body reference pose"),
    ("Λεωνίδας", "Leonidas: quiet boy about 5 years old, neat dark hair, gentle shy smile, full-body reference pose"),
]
for i, (name, desc) in enumerate(secondary, start=n2+1):
    assets.append({
        "id": f"A-{i:03d}", "cat": "👨‍👩‍👧 Δευτερεύοντες χαρακτήρες", "name": name,
        "prompt": f"Character reference sheet: {desc}, {BASE_STYLE}, plain neutral background, clean full-body character study, consistent with the book's overall style.",
        "priority": "HIGH" if name in ("Μαμά","Μπαμπάς") else "MEDIUM",
    })
n3 = n2 + len(secondary)

# Environmental props (7)
props = [
    ("Η ήρεμη γωνιά", "a cozy reading nook with a soft rug, floor cushion, small bookshelf, blanket, and a fairy-light string"),
    ("Η κούνια/παγκάκι παιδικής χαράς", "a colorful playground swing set beside a quiet wooden park bench under a tree"),
    ("Ένα δέντρο", "a friendly rounded-canopy tree, simple and iconic, suitable for a park or garden scene"),
    ("Το ποδήλατο της Μελίνας", "a small kids' bicycle without training wheels, pastel colors, a basket with flowers on front"),
    ("Το δωμάτιο της Μελίνας", "a cozy children's bedroom with a bed, bookshelf, window with curtains, warm evening light"),
    ("Η αίθουσα χορού", "a bright dance studio interior with a wall of mirrors and a wooden floor"),
    ("Το σαλόνι/κουζίνα", "a warm, lived-in family living-room/kitchen combo space with a sofa, TV, and dining table"),
]
for i, (name, desc) in enumerate(props, start=n3+1):
    assets.append({
        "id": f"A-{i:03d}", "cat": "🏡 Επαναλαμβανόμενα σκηνικά", "name": name,
        "prompt": f"Environment reference asset: {desc}, {BASE_STYLE}, no characters, empty scene ready to have characters added later.",
        "priority": "MEDIUM",
    })
n4 = n3 + len(props)

# Doodle stamps (6)
doodles = [
    ("Καρδιά", "a simple hand-drawn style heart doodle, thick outline, small sparkle accents"),
    ("Αστέρι", "a simple hand-drawn style star doodle, thick outline, rounded points"),
    ("Σύννεφο", "a simple hand-drawn style fluffy cloud doodle, thick outline"),
    ("Λουλούδι", "a simple hand-drawn style small flower doodle, five rounded petals, thick outline"),
    ("Πατούσα Μπισκότου", "a simple hand-drawn style paw-print doodle matching Biscuit's paw shape"),
    ("Μπαλόνι", "a simple hand-drawn style small party balloon doodle with a curly string"),
]
for i, (name, desc) in enumerate(doodles, start=n4+1):
    assets.append({
        "id": f"A-{i:03d}", "cat": "✨ Διακοσμητικά doodle stamps (γωνίες σελίδων)", "name": name,
        "prompt": f"Small decorative doodle stamp asset: {desc}, deep indigo linework (#2E2A47), transparent background, simple enough to scatter as a recurring page accent throughout the book.",
        "priority": "LOW",
    })

print(f"Assets: {len(assets)}")
print(f"TOTAL (scenes + assets): {len(scenes) + len(assets)}")

import json
with open("bible_data.json", "w", encoding="utf-8") as f:
    json.dump({"scenes": scenes, "assets": assets, "base_style": BASE_STYLE, "consistency": CONSISTENCY, "negative": NEGATIVE}, f, ensure_ascii=False)
