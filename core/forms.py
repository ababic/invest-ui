from django.conf import settings
from django.forms import Select, Textarea
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.translation import ugettext as _

from directory_components import forms, fields
from directory_constants.constants import choices


STAFF_CHOICES = (
    (
        'Less than 10',
        _('Less than 10')
    ),
    (
        '10 to 50',
        _('10 to 50')
    ),
    (
        '51 to 250',
        _('51 to 250')
    ),
    (
        'More than 250',
        _('More than 250')
    ),
)


class ContactForm(forms.Form):
    name = fields.CharField(
        label='Name',
    )
    job_title = fields.CharField(
        label='Job title',
    )
    email = fields.EmailField(
        label='Email address',
    )
    phone = fields.CharField(
        label='Phone number',
    )
    company_name = fields.CharField(
        label='Company name',
    )
    website_url = fields.URLField(
        label='Website url',
    )
    country = fields.ChoiceField(
        label='Which country are you based in?',
        widget=Select(attrs={'id': 'js-sector-select'}),
        choices=BLANK_CHOICE_DASH + [
            ("Afghanistan", "Afghanistan"),
            ("Albania", "Albania"),
            ("Algeria", "Algeria"),
            ("American Samoa", "American Samoa"),
            ("Andorra", "Andorra"),
            ("Angola", "Angola"),
            ("Anguilla", "Anguilla"),
            ("Antigua and Barbuda", "Antigua and Barbuda"),
            ("Argentina", "Argentina"),
            ("Armenia", "Armenia"),
            ("Aruba", "Aruba"),
            ("Australia", "Australia"),
            ("Austria", "Austria"),
            ("Azerbaijan", "Azerbaijan"),
            ("The Bahamas", "The Bahamas"),
            ("Bahrain", "Bahrain"),
            ("Bangladesh", "Bangladesh"),
            ("Barbados", "Barbados"),
            ("Belarus", "Belarus"),
            ("Belgium", "Belgium"),
            ("Belize", "Belize"),
            ("Benin", "Benin"),
            ("Bermuda", "Bermuda"),
            ("Bhutan", "Bhutan"),
            ("Bolivia", "Bolivia"),
            ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
            ("Botswana", "Botswana"),
            ("Brazil", "Brazil"),
            ("Brunei", "Brunei"),
            ("Bulgaria", "Bulgaria"),
            ("Burkina Faso", "Burkina Faso"),
            ("Burundi", "Burundi"),
            ("Cambodia", "Cambodia"),
            ("Cameroon", "Cameroon"),
            ("Canada", "Canada"),
            ("Cape Verde", "Cape Verde"),
            ("Cayman Islands", "Cayman Islands"),
            ("Central African Republic", "Central African Republic"),
            ("Chad", "Chad"),
            ("Chile", "Chile"),
            ("People 's Republic of China", "People 's Republic of China"),
            ("Republic of China", "Republic of China"),
            ("Christmas Island", "Christmas Island"),
            ("Cocos(Keeling) Islands", "Cocos(Keeling) Islands"),
            ("Colombia", "Colombia"),
            ("Comoros", "Comoros"),
            ("Congo", "Congo"),
            ("Cook Islands", "Cook Islands"),
            ("Costa Rica", "Costa Rica"),
            ("Cote d'Ivoire", "Cote d'Ivoire"),
            ("Croatia", "Croatia"),
            ("Cuba", "Cuba"),
            ("Cyprus", "Cyprus"),
            ("Czech Republic", "Czech Republic"),
            ("Denmark", "Denmark"),
            ("Djibouti", "Djibouti"),
            ("Dominica", "Dominica"),
            ("Dominican Republic", "Dominican Republic"),
            ("Ecuador", "Ecuador"),
            ("Egypt", "Egypt"),
            ("El Salvador", "El Salvador"),
            ("Equatorial Guinea", "Equatorial Guinea"),
            ("Eritrea", "Eritrea"),
            ("Estonia", "Estonia"),
            ("Ethiopia", "Ethiopia"),
            ("Falkland Islands", "Falkland Islands"),
            ("Faroe Islands", "Faroe Islands"),
            ("Fiji", "Fiji"),
            ("Finland", "Finland"),
            ("France", "France"),
            ("French Polynesia", "French Polynesia"),
            ("Gabon", "Gabon"),
            ("The Gambia", "The Gambia"),
            ("Georgia", "Georgia"),
            ("Germany", "Germany"),
            ("Ghana", "Ghana"),
            ("Gibraltar", "Gibraltar"),
            ("Greece", "Greece"),
            ("Greenland", "Greenland"),
            ("Grenada", "Grenada"),
            ("Guadeloupe", "Guadeloupe"),
            ("Guam", "Guam"),
            ("Guatemala", "Guatemala"),
            ("Guernsey", "Guernsey"),
            ("Guinea", "Guinea"),
            ("Guinea - Bissau", "Guinea - Bissau"),
            ("Guyana", "Guyana"),
            ("Haiti", "Haiti"),
            ("Honduras", "Honduras"),
            ("Hong Kong", "Hong Kong"),
            ("Hungary", "Hungary"),
            ("Iceland", "Iceland"),
            ("India", "India"),
            ("Indonesia", "Indonesia"),
            ("Iran", "Iran"),
            ("Iraq", "Iraq"),
            ("Ireland", "Ireland"),
            ("Israel", "Israel"),
            ("Italy", "Italy"),
            ("Jamaica", "Jamaica"),
            ("Japan", "Japan"),
            ("Jersey", "Jersey"),
            ("Jordan", "Jordan"),
            ("Kazakhstan", "Kazakhstan"),
            ("Kenya", "Kenya"),
            ("Kiribati", "Kiribati"),
            ("North Korea", "North Korea"),
            ("South Korea", "South Korea"),
            ("Kosovo", "Kosovo"),
            ("Kuwait", "Kuwait"),
            ("Kyrgyzstan", "Kyrgyzstan"),
            ("Laos", "Laos"),
            ("Latvia", "Latvia"),
            ("Lebanon", "Lebanon"),
            ("Lesotho", "Lesotho"),
            ("Liberia", "Liberia"),
            ("Libya", "Libya"),
            ("Liechtenstein", "Liechtenstein"),
            ("Lithuania", "Lithuania"),
            ("Luxembourg", "Luxembourg"),
            ("Macau", "Macau"),
            ("Macedonia", "Macedonia"),
            ("Madagascar", "Madagascar"),
            ("Malawi", "Malawi"),
            ("Malaysia", "Malaysia"),
            ("Maldives", "Maldives"),
            ("Mali", "Mali"),
            ("Malta", "Malta"),
            ("Marshall Islands", "Marshall Islands"),
            ("Martinique", "Martinique"),
            ("Mauritania", "Mauritania"),
            ("Mauritius", "Mauritius"),
            ("Mayotte", "Mayotte"),
            ("Mexico", "Mexico"),
            ("Micronesia", "Micronesia"),
            ("Moldova", "Moldova"),
            ("Monaco", "Monaco"),
            ("Mongolia", "Mongolia"),
            ("Montenegro", "Montenegro"),
            ("Montserrat", "Montserrat"),
            ("Morocco", "Morocco"),
            ("Mozambique", "Mozambique"),
            ("Myanmar", "Myanmar"),
            ("Nagorno - Karabakh", "Nagorno - Karabakh"),
            ("Namibia", "Namibia"),
            ("Nauru", "Nauru"),
            ("Nepal", "Nepal"),
            ("Netherlands", "Netherlands"),
            ("Netherlands Antilles", "Netherlands Antilles"),
            ("New Caledonia", "New Caledonia"),
            ("New Zealand", "New Zealand"),
            ("Nicaragua", "Nicaragua"),
            ("Niger", "Niger"),
            ("Nigeria", "Nigeria"),
            ("Niue", "Niue"),
            ("Norfolk Island", "Norfolk Island"),
            ("Turkish Republic of Northern Cyprus",
                "Turkish Republic of Northern Cyprus"),
            ("Northern Mariana", "Northern Mariana"),
            ("Norway", "Norway"),
            ("Oman", "Oman"),
            ("Pakistan", "Pakistan"),
            ("Palau", "Palau"),
            ("Palestine", "Palestine"),
            ("Panama", "Panama"),
            ("Papua New Guinea", "Papua New Guinea"),
            ("Paraguay", "Paraguay"),
            ("Peru", "Peru"),
            ("Philippines", "Philippines"),
            ("Pitcairn Islands", "Pitcairn Islands"),
            ("Poland", "Poland"),
            ("Portugal", "Portugal"),
            ("Puerto Rico", "Puerto Rico"),
            ("Qatar", "Qatar"),
            ("Romania", "Romania"),
            ("Russia", "Russia"),
            ("Rwanda", "Rwanda"),
            ("Saint Barthelemy", "Saint Barthelemy"),
            ("Saint Helena", "Saint Helena"),
            ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
            ("Saint Lucia", "Saint Lucia"),
            ("Saint Martin", "Saint Martin"),
            ("Saint Pierre and Miquelon", "Saint Pierre and Miquelon"),
            ("Saint Vincent and the Grenadines",
                "Saint Vincent and the Grenadines"),
            ("Samoa", "Samoa"),
            ("San Marino", "San Marino"),
            ("Sao Tome and Principe", "Sao Tome and Principe"),
            ("Saudi Arabia", "Saudi Arabia"),
            ("Senegal", "Senegal"),
            ("Serbia", "Serbia"),
            ("Seychelles", "Seychelles"),
            ("Sierra Leone", "Sierra Leone"),
            ("Singapore", "Singapore"),
            ("Slovakia", "Slovakia"),
            ("Slovenia", "Slovenia"),
            ("Solomon Islands", "Solomon Islands"),
            ("Somalia", "Somalia"),
            ("Somaliland", "Somaliland"),
            ("South Africa", "South Africa"),
            ("South Ossetia", "South Ossetia"),
            ("Spain", "Spain"),
            ("Sri Lanka", "Sri Lanka"),
            ("Sudan", "Sudan"),
            ("Suriname", "Suriname"),
            ("Svalbard", "Svalbard"),
            ("Swaziland", "Swaziland"),
            ("Sweden", "Sweden"),
            ("Switzerland", "Switzerland"),
            ("Syria", "Syria"),
            ("Taiwan", "Taiwan"),
            ("Tajikistan", "Tajikistan"),
            ("Tanzania", "Tanzania"),
            ("Thailand", "Thailand"),
            ("Timor - Leste", "Timor - Leste"),
            ("Togo", "Togo"),
            ("Tokelau", "Tokelau"),
            ("Tonga", "Tonga"),
            ("Transnistria Pridnestrovie", "Transnistria Pridnestrovie"),
            ("Trinidad and Tobago", "Trinidad and Tobago"),
            ("Tristan da Cunha", "Tristan da Cunha"),
            ("Tunisia", "Tunisia"),
            ("Turkey", "Turkey"),
            ("Turkmenistan", "Turkmenistan"),
            ("Turks and Caicos Islands", "Turks and Caicos Islands"),
            ("Tuvalu", "Tuvalu"),
            ("Uganda", "Uganda"),
            ("Ukraine", "Ukraine"),
            ("United Arab Emirates", "United Arab Emirates"),
            ("United Kingdom", "United Kingdom"),
            ("United States", "United States"),
            ("Uruguay", "Uruguay"),
            ("Uzbekistan", "Uzbekistan"),
            ("Vanuatu", "Vanuatu"),
            ("Vatican City", "Vatican City"),
            ("Venezuela", "Venezuela"),
            ("Vietnam", "Vietnam"),
            ("British Virgin Islands", "British Virgin Islands"),
            ("Isle of Man", "Isle of Man"),
            ("US Virgin Islands", "US Virgin Islands"),
            ("Wallis and Futuna", "Wallis and Futuna"),
            ("Western Sahara", "Western Sahara"),
            ("Yemen", "Yemen"),
            ("Zambia", "Zambia"),
            ("Zimbabwe", "Zimbabwe"),
        ]
    )

    number_of_staff = fields.ChoiceField(
        label='Which country are you based in?',
        choices=STAFF_CHOICES
    )
    investment_plans = fields.CharField(
        label=_('Tell us about your investment'),
        help_text=_('Tell us about your company and your plans for the UK in '
                    'terms of size of investment, operational and recruitment '
                    'plans. Please also tell us what help you would like from '
                    'the UK government.'),
        max_length=255,
        widget=Textarea()
    )


class SearchForm(forms.Form):

    term = fields.CharField(
        max_length=255,
        required=False,
    )
    sectors = fields.ChoiceField(
        required=False,
        choices=(
            (('', _('All industries')),) + choices.INDUSTRIES
        ),
        widget=Select(attrs={'class': 'bidi-rtl'})
    )


class LanguageForm(forms.Form):
    lang = fields.ChoiceField(
        choices=[]  # set by __init__
    )

    def __init__(self, language_choices=settings.LANGUAGES, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lang'].choices = language_choices

    def is_language_available(self, language_code):
        language_codes = [code for code, _ in self.fields['lang'].choices]
        return language_code in language_codes
