सबसे पहले खेत को चारो साइड से नाप लो| फिर किसी एक diagonal को measure कर लो, जो आसान हो| इस diagonal के एक head को 'b' माने|
फिर land_area_divider module के function में serially 'ab', 'bc', 'cd', 'da', 'bd', 'n' as arguments पास कर दे | n लोगों की संख्या है |
front side ko 'ab' maane aur kheto mein yah barabar bhago mein bategi|
iske samne ki side ya back side ko baatne ki width function return kar dega|

We can cut section from a field. in which we will not provide the value of n.
in this case we can fix a side with a length and app will return a length of unfix side for a given area.
this will give good result when we use graphical user interface.     (which is not yet implemented, in future it will be)