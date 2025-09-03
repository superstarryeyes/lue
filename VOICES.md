# Lue - Voices and Languages Guide

This document explains the speakers and languages included in the Edge and Kokoro TTS models, which are part of Lue’s default installation.

***

## Configuration

To configure voices and languages, edit the `lue/config.py` file:

```python
# Voice settings
TTS_VOICES = {
    "edge": "en-US-JennyNeural",  # Default Edge voice
    "kokoro": "af_heart",         # Default Kokoro voice
    "coqui": "path/to/your/voice.wav", # Default path to a Coqui speaker .wav
}

# Language settings for TTS models
TTS_LANGUAGE_CODES = {
    "kokoro": "a",  # Language code for Kokoro TTS
}
```

***

## Supported Languages and Codes

### Edge Model Language Codes

You don't need to specify language code for the Edge TTS model. Edge indicates the language in standard locale codes (e.g., `en-US`, `fr-FR`, `ja-JP`) within the speaker name. See the full list of Edge voices below.

### Kokoro Model Language Codes

When using Kokoro, make sure the `lang_code` matches your selected voice. For more detailed information, refer to Kokoro TTS documentation: https://github.com/hexgrad/kokoro.

| Language | Code | Notes |
| :--- | :--- | :--- |
| **American English** | `a` | Default language |
| **British English** | `b` | |
| **Spanish** | `e` | espeak-ng `es` fallback |
| **French** | `f` | espeak-ng `fr-fr` fallback |
| **Hindi** | `h` | espeak-ng `hi` fallback |
| **Italian** | `i` | espeak-ng `it` fallback |
| **Brazilian Portuguese**| `p` | espeak-ng `pt-br` fallback |
| **Japanese** | `j` | Requires `pip install misaki[ja]` |
| **Mandarin Chinese** | `z` | Requires `pip install misaki[zh]` |

### Coqui Model Language Codes

The Coqui XTTS model supports a variety of languages. Use the following codes with the --lang argument. For more details, refer to the [Coqui TTS Documentation](https://github.com/coqui-ai/TTS).

| Language | Code |
| :--- | :--- |
| English | en |
| Spanish | es |
| French | fr |
| German | de |
| Italian | it |
| Portuguese| pt |
| Polish | pl |
| Turkish | tr |
| Russian | ru |
| Dutch | nl |
| Czech | cs |
| Arabic | ar |
| Chinese (Mandarin) | zh-cn |
| Japanese | ja |
| Hungarian | hu |
| Korean | ko |

***

## Available Voices by Language

### Edge Voices

Edge TTS provides a wide variety of voices across many languages. Always include the full language code, country code, and voice name exactly as shown (e.g., en-US-JennyNeural):

#### Afrikaans (South Africa)

*   af-ZA-AdriNeural (Female)
*   af-ZA-WillemNeural (Male)

#### Albanian (Albania)

*   sq-AL-AnilaNeural (Female)
*   sq-AL-IlirNeural (Male)

#### Amharic (Ethiopia)

*   am-ET-AmehaNeural (Male)
*   am-ET-MekdesNeural (Female)

#### Arabic

*   ar-DZ-AminaNeural (Female) - Algeria
*   ar-DZ-IsmaelNeural (Male) - Algeria
*   ar-BH-AliNeural (Male) - Bahrain
*   ar-BH-LailaNeural (Female) - Bahrain
*   ar-EG-SalmaNeural (Female) - Egypt
*   ar-EG-ShakirNeural (Male) - Egypt
*   ar-IQ-BasselNeural (Male) - Iraq
*   ar-IQ-RanaNeural (Female) - Iraq
*   ar-JO-SanaNeural (Female) - Jordan
*   ar-JO-TaimNeural (Male) - Jordan
*   ar-KW-FahedNeural (Male) - Kuwait
*   ar-KW-NouraNeural (Female) - Kuwait
*   ar-LB-LaylaNeural (Female) - Lebanon
*   ar-LB-RamiNeural (Male) - Lebanon
*   ar-LY-ImanNeural (Female) - Libya
*   ar-LY-OmarNeural (Male) - Libya
*   ar-MA-JamalNeural (Male) - Morocco
*   ar-MA-MounaNeural (Female) - Morocco
*   ar-OM-AbdullahNeural (Male) - Oman
*   ar-OM-AyshaNeural (Female) - Oman
*   ar-QA-AmalNeural (Female) - Qatar
*   ar-QA-MoazNeural (Male) - Qatar
*   ar-SA-HamedNeural (Male) - Saudi Arabia
*   ar-SA-ZariyahNeural (Female) - Saudi Arabia
*   ar-SY-AmanyNeural (Female) - Syria
*   ar-SY-LaithNeural (Male) - Syria
*   ar-TN-HediNeural (Male) - Tunisia
*   ar-TN-ReemNeural (Female) - Tunisia
*   ar-AE-FatimaNeural (Female) - United Arab Emirates
*   ar-AE-HamdanNeural (Male) - United Arab Emirates
*   ar-YE-MaryamNeural (Female) - Yemen
*   ar-YE-SalehNeural (Male) - Yemen

#### Azerbaijani (Azerbaijan)

*   az-AZ-BabekNeural (Male)
*   az-AZ-BanuNeural (Female)

#### Bengali

*   bn-BD-NabanitaNeural (Female) - Bangladesh
*   bn-BD-PradeepNeural (Male) - Bangladesh
*   bn-IN-BashkarNeural (Male) - India
*   bn-IN-TanishaaNeural (Female) - India

#### Bosnian (Bosnia and Herzegovina)

*   bs-BA-GoranNeural (Male)
*   bs-BA-VesnaNeural (Female)

#### Bulgarian (Bulgaria)

*   bg-BG-BorislavNeural (Male)
*   bg-BG-KalinaNeural (Female)

#### Burmese (Myanmar)

*   my-MM-NilarNeural (Female)
*   my-MM-ThihaNeural (Male)

#### Catalan (Spain)

*   ca-ES-EnricNeural (Male)
*   ca-ES-JoanaNeural (Female)

#### Chinese

*   zh-HK-HiuGaaiNeural (Female) - Hong Kong
*   zh-HK-HiuMaanNeural (Female) - Hong Kong
*   zh-HK-WanLungNeural (Male) - Hong Kong
*   zh-CN-XiaoxiaoNeural (Female) - Mandarin
*   zh-CN-XiaoyiNeural (Female) - Mandarin
*   zh-CN-YunjianNeural (Male) - Mandarin
*   zh-CN-YunxiNeural (Male) - Mandarin
*   zh-CN-YunxiaNeural (Male) - Mandarin
*   zh-CN-YunyangNeural (Male) - Mandarin
*   zh-CN-liaoning-XiaobeiNeural (Female) - Liaoning
*   zh-TW-HsiaoChenNeural (Female) - Taiwanese Mandarin
*   zh-TW-YunJheNeural (Male) - Taiwanese Mandarin
*   zh-TW-HsiaoYuNeural (Female) - Taiwanese Mandarin
*   zh-CN-shaanxi-XiaoniNeural (Female) - Shaanxi

#### Croatian (Croatia)

*   hr-HR-GabrijelaNeural (Female)
*   hr-HR-SreckoNeural (Male)

#### Czech (Czech Republic)

*   cs-CZ-AntoninNeural (Male)
*   cs-CZ-VlastaNeural (Female)

#### Danish (Denmark)

*   da-DK-ChristelNeural (Female)
*   da-DK-JeppeNeural (Male)

#### Dutch

*   nl-BE-ArnaudNeural (Male) - Belgium
*   nl-BE-DenaNeural (Female) - Belgium
*   nl-NL-ColetteNeural (Female) - Netherlands
*   nl-NL-FennaNeural (Female) - Netherlands
*   nl-NL-MaartenNeural (Male) - Netherlands

#### English

*   en-AU-NatashaNeural (Female) - Australia
*   en-AU-WilliamNeural (Male) - Australia
*   en-CA-ClaraNeural (Female) - Canada
*   en-CA-LiamNeural (Male) - Canada
*   en-HK-SamNeural (Male) - Hong Kong
*   en-HK-YanNeural (Female) - Hong Kong
*   en-IN-NeerjaNeural (Female) - India
*   en-IN-PrabhatNeural (Male) - India
*   en-IE-ConnorNeural (Male) - Ireland
*   en-IE-EmilyNeural (Female) - Ireland
*   en-KE-AsiliaNeural (Female) - Kenya
*   en-KE-ChilembaNeural (Male) - Kenya
*   en-NZ-MitchellNeural (Male) - New Zealand
*   en-NZ-MollyNeural (Female) - New Zealand
*   en-NG-AbeoNeural (Male) - Nigeria
*   en-NG-EzinneNeural (Female) - Nigeria
*   en-PH-JamesNeural (Male) - Philippines
*   en-PH-RosaNeural (Female) - Philippines
*   en-SG-LunaNeural (Female) - Singapore
*   en-SG-WayneNeural (Male) - Singapore
*   en-ZA-LeahNeural (Female) - South Africa
*   en-ZA-LukeNeural (Male) - South Africa
*   en-TZ-ElimuNeural (Male) - Tanzania
*   en-TZ-ImaniNeural (Female) - Tanzania
*   en-GB-LibbyNeural (Female) - United Kingdom
*   en-GB-MaisieNeural (Female) - United Kingdom
*   en-GB-RyanNeural (Male) - United Kingdom
*   en-GB-SoniaNeural (Female) - United Kingdom
*   en-GB-ThomasNeural (Male) - United Kingdom
*   en-US-AriaNeural (Female) - United States
*   en-US-AnaNeural (Female) - United States
*   en-US-ChristopherNeural (Male) - United States
*   en-US-EricNeural (Male) - United States
*   en-US-GuyNeural (Male) - United States
*   **en-US-JennyNeural** (Female) - Default US English voice
*   en-US-MichelleNeural (Female) - United States
*   en-US-RogerNeural (Male) - United States
*   en-US-SteffanNeural (Male) - United States

#### Estonian (Estonia)

*   et-EE-AnuNeural (Female)
*   et-EE-KertNeural (Male)

#### Filipino (Philippines)

*   fil-PH-AngeloNeural (Male)
*   fil-PH-BlessicaNeural (Female)

#### Finnish (Finland)

*   fi-FI-HarriNeural (Male)
*   fi-FI-NooraNeural (Female)

#### French

*   fr-BE-CharlineNeural (Female) - Belgium
*   fr-BE-GerardNeural (Male) - Belgium
*   fr-CA-AntoineNeural (Male) - Canada
*   fr-CA-JeanNeural (Male) - Canada
*   fr-CA-SylvieNeural (Female) - Canada
*   fr-FR-DeniseNeural (Female) - France
*   fr-FR-EloiseNeural (Female) - France
*   fr-FR-HenriNeural (Male) - France
*   fr-CH-ArianeNeural (Female) - Switzerland
*   fr-CH-FabriceNeural (Male) - Switzerland

#### Galician (Spain)

*   gl-ES-RoiNeural (Male)
*   gl-ES-SabelaNeural (Female)

#### Georgian (Georgia)

*   ka-GE-EkaNeural (Female)
*   ka-GE-GiorgiNeural (Male)

#### German

*   de-AT-IngridNeural (Female) - Austria
*   de-AT-JonasNeural (Male) - Austria
*   de-DE-AmalaNeural (Female) - Germany
*   de-DE-ConradNeural (Male) - Germany
*   de-DE-KatjaNeural (Female) - Germany
*   de-DE-KillianNeural (Male) - Germany
*   de-CH-JanNeural (Male) - Switzerland
*   de-CH-LeniNeural (Female) - Switzerland

#### Greek (Greece)

*   el-GR-AthinaNeural (Female)
*   el-GR-NestorasNeural (Male)

#### Gujarati (India)

*   gu-IN-DhwaniNeural (Female)
*   gu-IN-NiranjanNeural (Male)

#### Hebrew (Israel)

*   he-IL-AvriNeural (Male)
*   he-IL-HilaNeural (Female)

#### Hindi (India)

*   hi-IN-MadhurNeural (Male)
*   hi-IN-SwaraNeural (Female)

#### Hungarian (Hungary)

*   hu-HU-NoemiNeural (Female)
*   hu-HU-TamasNeural (Male)

#### Icelandic (Iceland)

*   is-IS-GudrunNeural (Female)
*   is-IS-GunnarNeural (Male)

#### Indonesian (Indonesia)

*   id-ID-ArdiNeural (Male)
*   id-ID-GadisNeural (Female)

#### Irish (Ireland)

*   ga-IE-ColmNeural (Male)
*   ga-IE-OrlaNeural (Female)

#### Italian (Italy)

*   it-IT-DiegoNeural (Male)
*   it-IT-ElsaNeural (Female)
*   it-IT-IsabellaNeural (Female)

#### Japanese (Japan)

*   ja-JP-KeitaNeural (Male)
*   ja-JP-NanamiNeural (Female)

#### Javanese (Indonesia)

*   jv-ID-DimasNeural (Male)
*   jv-ID-SitiNeural (Female)

#### Kannada (India)

*   kn-IN-GaganNeural (Male)
*   kn-IN-SapnaNeural (Female)

#### Kazakh (Kazakhstan)

*   kk-KZ-AigulNeural (Female)
*   kk-KZ-DauletNeural (Male)

#### Khmer (Cambodia)

*   km-KH-PisethNeural (Male)
*   km-KH-SreymomNeural (Female)

#### Korean (Korea)

*   ko-KR-InJoonNeural (Male)
*   ko-KR-SunHiNeural (Female)

#### Lao (Laos)

*   lo-LA-ChanthavongNeural (Male)
*   lo-LA-KeomanyNeural (Female)

#### Latvian (Latvia)

*   lv-LV-EveritaNeural (Female)
*   lv-LV-NilsNeural (Male)

#### Lithuanian (Lithuania)

*   lt-LT-LeonasNeural (Male)
*   lt-LT-OnaNeural (Female)

#### Macedonian (North Macedonia)

*   mk-MK-AleksandarNeural (Male)
*   mk-MK-MarijaNeural (Female)

#### Malay (Malaysia)

*   ms-MY-OsmanNeural (Male)
*   ms-MY-YasminNeural (Female)

#### Malayalam (India)

*   ml-IN-MidhunNeural (Male)
*   ml-IN-SobhanaNeural (Female)

#### Maltese (Malta)

*   mt-MT-GraceNeural (Female)
*   mt-MT-JosephNeural (Male)

#### Marathi (India)

*   mr-IN-AarohiNeural (Female)
*   mr-IN-ManoharNeural (Male)

#### Mongolian (Mongolia)

*   mn-MN-BataaNeural (Male)
*   mn-MN-YesuiNeural (Female)

#### Nepali (Nepal)

*   ne-NP-HemkalaNeural (Female)
*   ne-NP-SagarNeural (Male)

#### Norwegian (Bokmål, Norway)

*   nb-NO-FinnNeural (Male)
*   nb-NO-PernilleNeural (Female)

#### Pashto (Afghanistan)

*   ps-AF-GulNawazNeural (Male)
*   ps-AF-LatifaNeural (Female)

#### Persian (Iran)

*   fa-IR-DilaraNeural (Female)
*   fa-IR-FaridNeural (Male)

#### Polish (Poland)

*   pl-PL-MarekNeural (Male)
*   pl-PL-ZofiaNeural (Female)

#### Portuguese

*   pt-BR-AntonioNeural (Male) - Brazil
*   pt-BR-FranciscaNeural (Female) - Brazil
*   pt-PT-DuarteNeural (Male) - Portugal
*   pt-PT-RaquelNeural (Female) - Portugal

#### Romanian (Romania)

*   ro-RO-AlinaNeural (Female)
*   ro-RO-EmilNeural (Male)

#### Russian (Russia)

*   ru-RU-DmitryNeural (Male)
*   ru-RU-SvetlanaNeural (Female)

#### Serbian (Serbia)

*   sr-RS-NicholasNeural (Male)
*   sr-RS-SophieNeural (Female)

#### Sinhala (Sri Lanka)

*   si-LK-SameeraNeural (Male)
*   si-LK-ThiliniNeural (Female)

#### Slovak (Slovakia)

*   sk-SK-LukasNeural (Male)
*   sk-SK-ViktoriaNeural (Female)

#### Slovenian (Slovenia)

*   sl-SI-PetraNeural (Female)
*   sl-SI-RokNeural (Male)

#### Somali (Somalia)

*   so-SO-MuuseNeural (Male)
*   so-SO-UbaxNeural (Female)

#### Spanish

*   es-AR-ElenaNeural (Female) - Argentina
*   es-AR-TomasNeural (Male) - Argentina
*   es-BO-MarceloNeural (Male) - Bolivia
*   es-BO-SofiaNeural (Female) - Bolivia
*   es-CL-CatalinaNeural (Female) - Chile
*   es-CL-LorenzoNeural (Male) - Chile
*   es-CO-GonzaloNeural (Male) - Colombia
*   es-CO-SalomeNeural (Female) - Colombia
*   es-CR-JuanNeural (Male) - Costa Rica
*   es-CR-MariaNeural (Female) - Costa Rica
*   es-CU-BelkysNeural (Female) - Cuba
*   es-CU-ManuelNeural (Male) - Cuba
*   es-DO-EmilioNeural (Male) - Dominican Republic
*   es-DO-RamonaNeural (Female) - Dominican Republic
*   es-EC-AndreaNeural (Female) - Ecuador
*   es-EC-LuisNeural (Male) - Ecuador
*   es-SV-LorenaNeural (Female) - El Salvador
*   es-SV-RodrigoNeural (Male) - El Salvador
*   es-GQ-JavierNeural (Male) - Equatorial Guinea
*   es-GQ-TeresaNeural (Female) - Equatorial Guinea
*   es-GT-AndresNeural (Male) - Guatemala
*   es-GT-MartaNeural (Female) - Guatemala
*   es-HN-CarlosNeural (Male) - Honduras
*   es-HN-KarlaNeural (Female) - Honduras
*   es-MX-DaliaNeural (Female) - Mexico
*   es-MX-JorgeNeural (Male) - Mexico
*   es-NI-FedericoNeural (Male) - Nicaragua
*   es-NI-YolandaNeural (Female) - Nicaragua
*   es-PA-MargaritaNeural (Female) - Panama
*   es-PA-RobertoNeural (Male) - Panama
*   es-PY-MarioNeural (Male) - Paraguay
*   es-PY-TaniaNeural (Female) - Paraguay
*   es-PE-AlexNeural (Male) - Peru
*   es-PE-CamilaNeural (Female) - Peru
*   es-PR-KarinaNeural (Female) - Puerto Rico
*   es-PR-VictorNeural (Male) - Puerto Rico
*   es-ES-AlvaroNeural (Male) - Spain
*   es-ES-ElviraNeural (Female) - Spain
*   es-US-AlonsoNeural (Male) - United States
*   es-US-PalomaNeural (Female) - United States
*   es-UY-MateoNeural (Male) - Uruguay
*   es-UY-ValentinaNeural (Female) - Uruguay
*   es-VE-PaolaNeural (Female) - Venezuela
*   es-VE-SebastianNeural (Male) - Venezuela

#### Sundanese (Indonesia)

*   su-ID-JajangNeural (Male)
*   su-ID-TutiNeural (Female)

#### Swahili

*   sw-KE-RafikiNeural (Male) - Kenya
*   sw-KE-ZuriNeural (Female) - Kenya
*   sw-TZ-DaudiNeural (Male) - Tanzania
*   sw-TZ-RehemaNeural (Female) - Tanzania

#### Swedish (Sweden)

*   sv-SE-MattiasNeural (Male)
*   sv-SE-SofieNeural (Female)

#### Tamil

*   ta-IN-PallaviNeural (Female) - India
*   ta-IN-ValluvarNeural (Male) - India
*   ta-MY-KaniNeural (Female) - Malaysia
*   ta-MY-SuryaNeural (Male) - Malaysia
*   ta-SG-AnbuNeural (Male) - Singapore
*   ta-SG-VenbaNeural (Female) - Singapore
*   ta-LK-KumarNeural (Male) - Sri Lanka
*   ta-LK-SaranyaNeural (Female) - Sri Lanka

#### Telugu (India)

*   te-IN-MohanNeural (Male)
*   te-IN-ShrutiNeural (Female)

#### Thai (Thailand)

*   th-TH-NiwatNeural (Male)
*   th-TH-PremwadeeNeural (Female)

#### Turkish (Turkey)

*   tr-TR-AhmetNeural (Male)
*   tr-TR-EmelNeural (Female)

#### Ukrainian (Ukraine)

*   uk-UA-OstapNeural (Male)
*   uk-UA-PolinaNeural (Female)

#### Urdu

*   ur-IN-GulNeural (Female) - India
*   ur-IN-SalmanNeural (Male) - India
*   ur-PK-AsadNeural (Male) - Pakistan
*   ur-PK-UzmaNeural (Female) - Pakistan

#### Uzbek (Uzbekistan)

*   uz-UZ-MadinaNeural (Female)
*   uz-UZ-SardorNeural (Male)

#### Vietnamese (Vietnam)

*   vi-VN-HoaiMyNeural (Female)
*   vi-VN-NamMinhNeural (Male)

#### Welsh (United Kingdom)

*   cy-GB-AledNeural (Male)
*   cy-GB-NiaNeural (Female)

#### Zulu (South Africa)

*   zu-ZA-ThandoNeural (Female)
*   zu-ZA-ThembaNeural (Male)

***

### Kokoro Voices

#### American English (`lang_code='a'`)

*   **af_heart** (Female)
*   af_alloy (Female)
*   af_aoede (Female)
*   af_bella (Female)
*   af_jessica (Female)
*   af_kore (Female)
*   af_nicole (Female)
*   af_nova (Female)
*   af_river (Female)
*   af_sarah (Female)
*   af_sky (Female)
*   am_adam (Male)
*   am_echo (Male)
*   am_eric (Male)
*   am_fenrir (Male)
*   am_liam (Male)
*   am_michael (Male)
*   am_onyx (Male)
*   am_puck (Male)
*   am_santa (Male)

#### British English (`lang_code='b'`)

*   bf_alice (Female)
*   bf_emma (Female)
*   bf_isabella (Female)
*   bf_lily (Female)
*   bm_daniel (Male)
*   bm_fable (Male)
*   bm_george (Male)
*   bm_lewis (Male)

#### Japanese (`lang_code='j'`)

*   jf_alpha (Female)
*   jf_gongitsune (Female)
*   jf_nezumi (Female)
*   jf_tebukuro (Female)
*   jm_kumo (Male)

#### Mandarin Chinese (`lang_code='z'`)

*   zf_xiaobei (Female)
*   zf_xiaoni (Female)
*   zf_xiaoxiao (Female)
*   zf_xiaoyi (Female)
*   zm_yunjian (Male)
*   zm_yunxi (Male)
*   zm_yunxia (Male)
*   zm_yunyang (Male)

#### Spanish (`lang_code='e'`)

*   ef_dora (Female)
*   em_alex (Male)
*   em_santa (Male)

#### French (`lang_code='f'`)

*   ff_siwis (Female)

#### Hindi (`lang_code='h'`)

*   hf_alpha (Female)
*   hf_beta (Female)
*   hm_omega (Male)
*   hm_psi (Male)

#### Italian (`lang_code='i'`)

*   if_sara (Female)
*   im_nicola (Male)

#### Brazilian Portuguese (`lang_code='p'`)

*   pf_dora (Female)
*   pm_alex (Male)
*   pm_santa (Male)
