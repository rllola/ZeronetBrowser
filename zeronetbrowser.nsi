!define ZIP2EXE_COMPRESSOR_ZLIB
!define ZIP2EXE_INSTALLDIR "$PROGRAMFILES\Zeronet Browser"
!define ZIP2EXE_NAME "Zeronet Browser"
!define ZIP2EXE_OUTFILE "ZeronetBrowser_${TAG}_setup.exe"

!define MUI_ICON "icons\zeronet-logo.ico"

!define APPNAME "Zeronet Browser"
!define DESCRIPTION "A browser for ZeroNet"
# These three must be integers
!define VERSIONMAJOR ${MAJOR}
!define VERSIONMINOR ${MINOR}
!define VERSIONBUILD ${BUILD}
# These will be displayed by the "Click here for support information" link in "Add/Remove Programs"
# It is possible to use "mailto:" links in here to open the email client
!define HELPURL "https://github.com/rllola/ZeronetBrowser/" # "Support Information" link
!define UPDATEURL "https://github.com/rllola/ZeronetBrowser/releases" # "Product Updates" link
!define ABOUTURL "https://github.com/rllola/ZeronetBrowser/" # "Publisher" link
# This is the size (in kB) of all the files copied into "Program Files"
!define INSTALLSIZE ${SIZE}

!include "${NSISDIR}\Contrib\zip2exe\Base.nsh"
!include "${NSISDIR}\Contrib\zip2exe\Modern.nsh"

!insertmacro SECTION_BEGIN
File /r "dist\ZeronetBrowser\*.*"
!insertmacro SECTION_END

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
        messageBox mb_iconstop "Administrator rights required!"
        setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
        quit
${EndIf}
!macroend

section "install"

  # Create a user directory for the site and data
  CreateDirectory "$APPDATA\${APPNAME}\data"

  FileOpen $0 "$APPDATA\${APPNAME}\data\lock.pid" w
  FileClose $0

  FileOpen $0 "$APPDATA\${APPNAME}\zeronet.conf" w
  FileWrite $0 "[global]$\n"
  FileWrite $0 "data_dir = $APPDATA\${APPNAME}$\n"
  FileWrite $0 "log_dir = $APPDATA\${APPNAME}\log$\n"
  FileClose $0

  # Uninstaller - See function un.onInit and section "uninstall" for configuration
  writeUninstaller "$INSTDIR\uninstall.exe"

  # Start Menu
  createDirectory "$SMPROGRAMS\${APPNAME}"
  createShortCut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\${ZIP2EXE_OUTFILE}" "" "$INSTDIR\${MUI_ICON}"

  # Registry information for add/remove programs
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayName" "${APPNAME} - ${DESCRIPTION}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayIcon" "$\"$INSTDIR\${MUI_ICON}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "Publisher" "Lola"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "HelpLink" "$\"${HELPURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLUpdateInfo" "$\"${UPDATEURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "URLInfoAbout" "$\"${ABOUTURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "DisplayVersion" "$\"${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}$\""
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "VersionMinor" ${VERSIONMINOR}
	# There is no option for modifying or repairing the install
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoModify" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "NoRepair" 1
	# Set the INSTALLSIZE constant (!defined at the top of this script) so Add/Remove Programs can accurately report the size
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}" "EstimatedSize" ${INSTALLSIZE}

  WriteRegStr HKLM "Software\Classes\zero" "" "URL:ZeroNet Protocol"
  WriteRegStr HKLM "Software\Classes\zero" "ZeroNet" "Zero protocol"
  WriteRegStr HKLM "Software\Classes\zero" "URL Protocol" ""
  ; Optional: UseOriginalUrlEncoding
  WriteRegExpandStr HKLM "Software\Classes\zero\DefaultIcon" "" "$INSTDIR\ZeronetBrowser.exe"
  WriteRegStr HKLM "Software\Classes\zero\shell" "" "open"
  WriteRegStr HKLM "Software\Classes\zero\shell\open" "Zeronet Browser" "Open ZeroNet page in Zeronet Browser"
  WriteRegStr HKLM "Software\Classes\zero\shell\open\command" "" "$INSTDIR\ZeronetBrowser.exe %1"

sectionEnd

# Uninstaller

function un.onInit
	SetShellVarContext all

	#Verify the uninstaller - last chance to back out
	MessageBox MB_OKCANCEL "Permanantly remove ${APPNAME}?" IDOK next
		Abort
	next:
	!insertmacro VerifyUserIsAdmin
functionEnd

section "uninstall"

	# Remove Start Menu launcher
	delete "$SMPROGRAMS\${APPNAME}.lnk"
	# Try to remove the Start Menu folder - this will only happen if it is empty
	rmDir "$SMPROGRAMS\${APPNAME}"

	# Always delete uninstaller as the last action
	delete $INSTDIR\uninstall.exe

	# Try to remove the install directory
	rmDir /r $INSTDIR

	# Remove uninstaller information from the registry
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPNAME}"
  DeleteRegKey HKLM "Software\Classes\zero"
sectionEnd
