export targetPath=ipa
export appName=掌上盛京医院
export ipaType=AdHocExportOptions.plist

xcodebuild archive -archivePath "$targetPath/$appName.xcarchive" -workspace "./platforms/ios/$appName.xcworkspace" -sdk iphoneos -scheme "$appName" -configuration Release DEVELOPMENT_TEAM=Y6723Q456E CODE_SIGN_IDENTITY="iPhone Developer"
xcodebuild -exportArchive -archivePath "$targetPath/$appName.xcarchive" -exportPath "$targetPath/" -exportOptionsPlist $targetPath/$ipaType
