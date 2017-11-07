Pod::Spec.new do |spec|
  spec.name             = "BbStudentSDK"
  spec.version          = "3.2.2.5"
  spec.author           = { "iOS Developers" => "fu.liu@blackboard.com" }
  spec.source           = { :http => "http://maven.bbpd.io/content/repositories/bb-mobile-sdk-ios/com/blackboard/mobile-sdk/ios/BBMobileSDK.Student/3.2.2-dev-new.5/BBMobileSDK.Student-3.2.2-dev-new.5.zip", :sha1 => "139dea5d6cdc5fd4a39293133f50a036f0634d34"}
  spec.homepage         = "http://maven.bbpd.io/content/repositories/bb-mobile-sdk-ios/com/blackboard/mobile-sdk/ios/BBMobileSDK.Student/"
  spec.license          = 'Copyright © 2017 blackboard. All rights reserved.'
  spec.summary          = "Blackboard Mobile SDK for BbStuduent"

  spec.platform     = :ios, '9.0'
  spec.requires_arc = true

  spec.vendored_frameworks = ['ios-bbstudent-sdk/BBStudent.framework']
  spec.module_name = 'BbStudentSDK'

end
