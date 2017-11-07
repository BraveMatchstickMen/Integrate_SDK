Pod::Spec.new do |spec|
  spec.name             = "BbInstructorSDK"
  spec.version          = "3.2.3.1"
  spec.author           = { "iOS Developers" => "fu.liu@blackboard.com" }
  spec.source           = { :http => 'http://maven.bbpd.io/content/repositories/bb-mobile-sdk-ios/com/blackboard/mobile-sdk/ios/BBMobileSDK.Instructor/3.2.3-feature_student_offlinefeature_NUE-new.1/BBMobileSDK.Instructor-3.2.3-feature_student_offlinefeature_NUE-new.1.zip', :sha1 => '1eccc78789152b6c614b40f0d6bba812062f3c9e'}
  spec.homepage         = "http://maven.bbpd.io/content/repositories/bb-mobile-sdk-ios/com/blackboard/mobile-sdk/ios/BBMobileSDK.Instructor/"
  spec.license          = 'Copyright © 2017 blackboard. All rights reserved.'
  spec.summary          = "Blackboard Mobile SDK for BBInstructor"

  spec.platform     = :ios, '9.0'
  spec.requires_arc = true

  spec.vendored_frameworks = ['ios-bbinstructor-sdk/BBInstructor.framework']
  spec.module_name = 'BbInstructorSDK'

end
