# This is your project root, configure your own path.
# Make sure to include a trailing /
DATA_DIR = '/home/sophie/GitHub/transcript/Example/'

#### Options ####

# used by ttf.py to access full original fonts to compare with the broken ones
FULL_FONTS_PATH  = '/usr/share/fonts'

# remove mumbo-jumbo TEXT strings before HTML processing (REGEXes or text)
REMOVE_BEFORE = (
    r'The Office for Standards.*?www\.ofsted\.gov\.uk',
    r'Any complaints.*?\@ofsted\.gov\.uk',
    r'© Crown copyright 20\d\d',
    r'Inspection grades:.*?inspection terms',
    r'This letter.*?their school\.',
    r'You can use Parent View.*?www\.ofsted\.gov\.uk'
)

# find and replace after HTML processing finished
REPLACE_AFTER = (
    (r'td>( )?Overall effectiveness j', 'td colspan=4>Overall effectiveness j'),
)

# Additional bullet point characters to be expected at start of line for <li>
# Copied out of the processsed PDF. Common bullets are pre-programmed.
BULLETS =  ('', '')
