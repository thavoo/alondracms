define(['angular'],function(angular){
    angular.module('app.I18N.EN', [])
    .config(['$translateProvider', function ($translateProvider) 
    {
      	$translateProvider.translations('en', {
            'TITLE_LABEL': 'Title',
            'FILE_PLURAL_LABEL': 'Files',
            'THUMBNAIL_LABEL':'Thumbnail',
            'THUMBNAIL_TEXT_LABEL':'Thumbnail Text',
            'FEATURED_IMAGE_LABEL':'Featured Image',
            'FEATURED_IMAGE_TEXT_LABEL':'Featured Image Text',
            'LIST_LABEL': 'List',
            'EDIT_LABEL': 'Edit',
            'NEW_LABEL': 'New',
            'DELETE_LABEL': 'Delete',
            'UPDATE_LABEL': 'Update',
            'ACTIONS_LABEL': 'Actions',
            'CREATED_LABEL': 'Created',
            'UPDATED_LABEL': 'Updated',
            'PUBLISHED_LABEL': 'Published',
            'THUMB_LABEL': 'Thumb',
            'SAVE_LABEL': 'Save',
            'POST_LABEL': 'Post',
            'POST_PLURAL_LABEL': 'Posts',   
            'SEARCH_LABEL': 'Search',
            'CONTENT_LABEL': 'Content',
            'CATEGORIES_LABEL': 'Categories',
            'MEDIA_LABEL': 'Media',
            'IMAGE_LABEL': 'Imagen',
            'MEDIA_EXTERNAL_LABEL': 'Media External', 
            'THUMBNAIL_LABEL': 'Thumb',  
            'FEATURED_LABEL': 'Featured',  
            'SEARCH_FOR_LABEL': 'Search for...',  
            'IMAGE_PLURAL_LABEL': 'Images',  
            'USER_PLURAL_LABEL': 'Users',  
            'USER_LABEL': 'User', 
            'FIRST_NAME_LABEL': 'First name',
            'LAST_NAME_LABEL': 'Last Name',
            'COMPANY_NAME_LABEL': 'Company',
            'EMAIL_NAME_LABEL': 'Email',
            'NICK_NAME_LABEL': 'Nick',
            'ADDRESS_LABEL': 'Address',
            'ADDRESS_LINE_2_LABEL': 'Address line 2',
            'SELECT_COUNTRY_LABEL': 'Select country',
            'ZIP_CODE_LABEL': 'Zip code',
            'WEBSITE_LABEL': 'website',
            'JOB_POSITION_LABEL': 'Job Position',
            'JOB_DESCRIPTION_LABEL': 'Job Description',
            'MOBILE_PHONE_LABEL': 'Mobile phone',
            'DESCRIPTION_LABEL': 'About You',
            'SECRECT_QUESTION_LABEL': 'Secrect Question',
            'SECRECT_ANSWER_LABEL': 'Secrect Answer',
            'OLD_PASSWORD_LABEL': 'Old password',
            'NEW_PASSWORD_LABEL': 'New password',
            'REPEAT_NEW_PASSWORD_LABEL': 'Repeat new password',
            'CHANGE_PASSWORD_LABEL': 'change password',
            'GROUPS_LABEL': 'Group',
            'GROUPS_PLURAL_LABEL': 'Groups',
            'ADVIABLE_PERMISIONS_PLURAL_LABEL': 'Available permissions',
            'ADVIABLE_CHOSSEN_PLURAL_LABEL': 'Chossen permissions',
            'COMMENTS_LABEL': 'Comments',
            'THEMES_LABEL': 'Themes',
            'SEO_LABEL': 'Seo',
            'META_TITLE_LABEL': 'Meta Title',
            'META_DESCRIPTION_LABEL': 'Meta Description',
            'SLUG_LABEL': 'Slug',
            'CATEGORY_LABEL': 'Category',
            'CATEGORY_PLURAL_LABEL': 'Categories',
            'PUBLISH_LABEL':'Publish',
            'USERNAME_LABEL':'User',
            'DROP_FILES_LABEL':'Drop files here and upload',
            'UNLOADED_FILES_LABEL':'Your files are not actually uploaded.',
            'NAVIGATION_PLURAL_LABEL':'Navigation',
            'NAVIGATION_ITEMS_PLURAL_LABEL': 'Navigation Item',
            'DRAG_ELEMENTS_LABEL':'Drag Elements',
            'ON_FEED_LABEL':'On Feed?',
            'FEATURED_LABEL':'Featured',
            'TAGS_LABEL':'Tags',
            'PAGES_LABEL':'Page',
            'PAGES_PLURAL_LABEL':'Pages',
            'GAME_LABEL':'Game',
            'GAME_PLURAL_LABEL':'Games',
            'VIDEO_LABEL':'Video',
            'VIDEO_PLURAL_LABEL':'Videos',
            'GAME_ENGINE_LABEL':'Game Engine',
            'GAME_ENGINE_PLURAL_LABEL':'Game Engines',
            'EXCERPT_LABEL':'Excerpt',
            'MEDIA_ALBUM_PLURAL_LABEL':'Media Albums',
            'MEDIA_ALBUM_LABEL':'Media Album',
            'ITEMS_PLURAL_LABEL':'Items',
            'LINK_LABEL':'Link/url'
      });
     
      $translateProvider.preferredLanguage('en');
    }]);
});
