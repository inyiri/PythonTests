import os
import sys
import zipfile
from shutil import copy

def getArtifactName( artifactHome ):
    for file in os.listdir( artifactHome ):
        if ( file.endswith('*.jar') ):
            return file;
    return '';

# It works both EAR and WAR files
def getManifestVersion(fileName):
    lstr = '';
    WLTEXT = 'Weblogic-Application-Version:';

    zf = zipfile.ZipFile(fileName, 'r');
    f = zf.open('META-INF/MANIFEST.MF', 'r');
    
    lines = f.readlines();
    f.close();
    zf.close();
    for line in lines:
        lstr = str(line, 'utf-8');
        lstr = lstr.strip();
        if ( lstr.startswith( WLTEXT ) ):
            lstr = lstr.replace( WLTEXT, '');
            lstr = lstr.strip();
            break;
    return lstr; 

def copyFile(artifactHome, appHome):
    artifactFileName = artifactHome + '/' + getArtifactName( artifactHome );
    subdir = getManifestVersion( artifactFileName );
    targetDir = appHome + '/' + subdir;
    os.mkdir( targetDir );
    copy( artifactFileName, targetDir );    



# Start program here 
# Sample: python3 copyCICD.py /home/inyiri/tanulas/python/alma.ear /home/inyiri/tanulas/python/ide
artifactHome = sys.argv[1];
appHome = sys.argv[2];

 
# copyFile(artifact, appHome);

# print(artifact);
# print(appHome);
