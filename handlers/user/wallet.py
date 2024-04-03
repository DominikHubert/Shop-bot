
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import balance

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=balance)
async def process_balance(message: Message, state: FSMContext):
    smessage = f'''Es ist wichtig zu beachten, dass ich kein Arzt bin, und diese Liste keine vollständige medizinische Beratung ersetzen kann. Darüber hinaus können die Prävalenz und Relevanz von Volkskrankheiten je nach Region und Bevölkerungsgruppe variieren. Hier sind jedoch einige häufige Volkskrankheiten: \n
1.	Herz-Kreislauf-Erkrankungen: Hierzu gehören Herzinfarkte, Schlaganfälle, Bluthochdruck und Herzinsuffizienz. \n
2.	Diabetes: Typ-2-Diabetes ist weit verbreitet und resultiert oft aus einer Kombination von genetischer Veranlagung und Lebensstilfaktoren.\n
3.	Atemwegserkrankungen: Dazu gehören Asthma, chronisch obstruktive Lungenerkrankung (COPD) und Atemnotsyndrom.\n
4.	Krebs: Verschiedene Arten von Krebs, wie Lungenkrebs, Brustkrebs, Darmkrebs und Prostatakrebs, sind häufige Ursachen für Krankheiten und Todesfälle.\n
5.	Psychische Gesundheitsprobleme: Dazu zählen Depressionen, Angststörungen, bipolare Störungen und Schizophrenie.\n
6.	Adipositas: Übergewicht und Fettleibigkeit können zu verschiedenen Gesundheitsproblemen führen, darunter Diabetes, Herzkrankheiten und Gelenkprobleme.\n
7.	Osteoporose: Ein Zustand, bei dem die Knochen an Dichte verlieren und brüchig werden.\n
8.	Alzheimer-Krankheit: Eine fortschreitende neurologische Erkrankung, die Gedächtnisverlust und kognitive Beeinträchtigungen verursacht.\n
9.	Arthritis: Eine Gruppe von Erkrankungen, die Gelenkentzündungen verursachen, wie rheumatoide Arthritis und Osteoarthritis.\n
10.	Chronisch entzündliche Darmerkrankungen (CED): Hierzu gehören Morbus Crohn und Colitis ulcerosa.\n
Es ist wichtig zu betonen, dass die Prävention, Früherkennung und angemessene Behandlung entscheidend sind, um das Risiko und den Schweregrad dieser Krankheiten zu minimieren. Bei gesundheitlichen Bedenken sollten Sie immer einen Arzt oder Facharzt konsultieren.\n
Omega-3-Fettsäuren, insbesondere Eicosapentaensäure (EPA) und Docosahexaensäure (DHA), werden mit verschiedHerz-Kreislauf-Erkrankungen: Omega-3-Fettsäuren haben nachweislich positive Auswirkungen auf das Herz-Kreislauf-System. Sie können den Blutdruck senken, die Triglyceridwerte reduzieren, die Blutfettwerte verbessern und Entzündungen im Körper verringern, was das Risiko von Herzkrankheiten reduzieren kann.enen gesundheitlichen Vorteilen in Verbindung gebracht. Hier sind einige Volkskrankheiten, bei denen Omega-3-Fettsäuren unterstützend wirken können:\n
1.	Diabetes: Omega-3-Fettsäuren könnten bei der Verbesserung der Insulinsensitivität helfen und Entzündungen reduzieren, was für Menschen mit Diabetes Typ 2 vorteilhaft sein kann.\n
2.	Psychische Gesundheitsprobleme: Einige Studien legen nahe, dass Omega-3-Fettsäuren positive Auswirkungen auf die Stimmung haben können und bei der Prävention von Depressionen und Angststörungen unterstützend wirken könnten.\n
3.	Entzündliche Erkrankungen: Omega-3-Fettsäuren haben entzündungshemmende Eigenschaften, was sie bei entzündlichen Erkrankungen wie rheumatoider Arthritis oder chronisch entzündlichen Darmerkrankungen (CED) unterstützend machen könnte.\n
4.	Neurologische Gesundheit: Omega-3-Fettsäuren, insbesondere DHA, sind ein wichtiger Bestandteil der Gehirnzellen. Es wird vermutet, dass sie die kognitive Funktion unterstützen und das Risiko von neurodegenerativen Erkrankungen wie Alzheimer und Demenz verringern können.\n


'''
    smessage2 = f'''Es ist wichtig zu beachten, dass Omega-3-Fettsäuren allein keine Heilmittel für diese Krankheiten sind. Sie können jedoch Teil einer gesunden Ernährung und eines gesunden Lebensstils sein. Fischölpräparate sind eine häufige Quelle für Omega-3-Fettsäuren, aber es ist ratsam, vor der Einnahme von Nahrungsergänzungsmitteln einen Arzt zu konsultieren, um die richtige Dosierung und mögliche Wechselwirkungen mit anderen Medikamenten zu besprechen. Eine ausgewogene Ernährung mit Fisch, Nüssen, Samen und pflanzlichen Ölen kann ebenfalls eine natürliche Quelle für Omega-3-Fettsäuren sein.\n
1.	Atemwegserkrankungen:\n
o	Entzündungshemmende Eigenschaften könnten bei Asthma und COPD vorteilhaft sein, indem sie Entzündungen in den Atemwegen reduzieren.\n
2.	Krebserkrankungen:\n
o	Es gibt Hinweise darauf, dass Omega-3-Fettsäuren das Wachstum bestimmter Krebsarten hemmen können, aber die Forschung ist hier noch im Gange. Insbesondere könnten sie in Kombination mit konventionellen Therapien unterstützend wirken.\n
3.	Infektionskrankheiten:\n
o	Omega-3-Fettsäuren können das Immunsystem stärken und entzündungshemmende Eigenschaften haben, was bei der Prävention von Infektionskrankheiten hilfreich sein kann.\n
4.	Stoffwechselstörungen:\n
o	Omega-3-Fettsäuren könnten den Fettstoffwechsel verbessern und Entzündungen reduzieren, was bei Stoffwechselstörungen wie Gicht vorteilhaft sein kann.\n
5.	Neurologische Erkrankungen:\n
o	Omega-3-Fettsäuren könnten neuroprotektive Eigenschaften haben, die bei neurologischen Erkrankungen wie Schlaganfall, Migräne, Parkinson-Krankheit und ALS unterstützend wirken könnten.\n
6.	Augenkrankheiten:\n
o	Omega-3-Fettsäuren, insbesondere DHA, sind wichtig für die Augengesundheit und könnten das Risiko von Augenerkrankungen wie Altersbedingter Makuladegeneration (AMD), Glaukom und diabetischer Retinopathie verringern.\n
7.	Nierenerkrankungen:\n
o	Entzündungshemmende Wirkungen könnten bei chronischer Niereninsuffizienz und Nephritis unterstützend sein.\n
8.	Endokrine Erkrankungen/Schilddrüse:\n
o	Omega-3-Fettsäuren könnten Entzündungen reduzieren, was bei endokrinen Erkrankungen wie Schilddrüsenerkrankungen, PCOS und Morbus Cushing vorteilhaft sein kann.\n
9.	Muskuloskelettale Erkrankungen:\n
o	Entzündungshemmende Eigenschaften könnten bei entzündlichen Gelenkerkrankungen wie rheumatoider Arthritis unterstützend wirken. Omega-3-Fettsäuren könnten auch die Knochendichte unterstützen und somit Osteoporose vorbeugen.\n
10.	Hauterkrankungen:\n
o	Entzündungshemmende Wirkungen könnten bei Hauterkrankungen wie Ekzemen, Psoriasis und Akne unterstützend sein.\n
Es ist wichtig zu betonen, dass die individuellen Reaktionen auf Omega-3-Fettsäuren variieren können, und Nahrungsergänzungsmittel sollten in Absprache mit einem Arzt eingenommen werden. Omega-3-Fettsäuren können Teil einer gesunden Lebensweise sein, aber sie sollten nicht als Ersatz für medizinische Behandlungen betrachtet werden.\n'''
    smessage3 = '''Studien:\n
1.	Herz-Kreislauf-Erkrankungen:\n
o	Mozaffarian, D., & Wu, J. H. (2011). Omega-3 Fatty Acids and Cardiovascular Disease: Effects on Risk Factors, Molecular Pathways, and Clinical Events. Journal of the American College of Cardiology, 58(20), 2047–2067.\n
2.	Diabetes:\n
o	Wu, J. H., Micha, R., Imamura, F., Pan, A., Biggs, M. L., Ajaz, O., ... & Mozaffarian, D. (2017). Omega-3 fatty acids and incident type 2 diabetes: a systematic review and meta-analysis. Diabetologia, 60(12), 2241-2250.\n
3.	Psychische Gesundheitsprobleme:\n
o	Grosso, G., Pajak, A., Marventano, S., Castellano, S., Galvano, F., Bucolo, C., ... & Caraci, F. (2014). Role of omega-3 fatty acids in the treatment of depressive disorders: a comprehensive meta-analysis of randomized clinical trials. PloS One, 9(5), e96905.\n
4.	Entzündliche Erkrankungen:\n
o	Calder, P. C. (2013). Omega-3 polyunsaturated fatty acids and inflammatory processes: nutrition or pharmacology? British Journal of Clinical Pharmacology, 75(3), 645–662.\n
5.	Neurologische Gesundheit:\n
o	Burckhardt, M., & Herke, M. (2014). Omega-3 fatty acids for the treatment of dementia. The Cochrane Database of Systematic Reviews, 6, CD009002.\n
6.	Atemwegserkrankungen:\n
o	Wood, L. G., Garg, M. L., & Gibson, P. G. (2015). A high-fat challenge increases airway inflammation and impairs bronchodilator recovery in asthma. Journal of Allergy and Clinical Immunology, 136(4), 938-947.\n
'''
    await message.answer(smessage)
    await message.answer(smessage2)
    await message.answer(smessage3)
