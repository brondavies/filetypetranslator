﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System.Xml.Serialization;

// 
// This source code was auto-generated by xsd, Version=4.0.30319.33440.
// 


/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
[System.Xml.Serialization.XmlRootAttribute(Namespace="http://www.freedesktop.org/standards/shared-mime-info", IsNullable=false)]
public partial class match {
    
    private match[] match1Field;
    
    private string typeField;
    
    private string valueField;
    
    private string offsetField;
    
    private string maskField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("match")]
    public match[] match1 {
        get {
            return this.match1Field;
        }
        set {
            this.match1Field = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string type {
        get {
            return this.typeField;
        }
        set {
            this.typeField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string value {
        get {
            return this.valueField;
        }
        set {
            this.valueField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string offset {
        get {
            return this.offsetField;
        }
        set {
            this.offsetField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string mask {
        get {
            return this.maskField;
        }
        set {
            this.maskField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
[System.Xml.Serialization.XmlRootAttribute("mime-info", Namespace="http://www.freedesktop.org/standards/shared-mime-info", IsNullable=false)]
public partial class MimeInfo {
    
    private object[] itemsField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("match", typeof(match))]
    [System.Xml.Serialization.XmlElementAttribute("mime-type", typeof(mimeinfoMimetype))]
    public object[] Items {
        get {
            return this.itemsField;
        }
        set {
            this.itemsField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetype {
    
    private string _commentField;
    
    private string acronymField;
    
    private string expandedacronymField;
    
    private mimeinfoMimetypeSubclassof[] subclassofField;
    
    private mimeinfoMimetypeGenericicon[] genericiconField;
    
    private mimeinfoMimetypeGlob[] globField;
    
    private mimeinfoMimetypeMagic[] magicField;
    
    private mimeinfoMimetypeAlias[] aliasField;
    
    private mimeinfoMimetypeRootXML[] rootXMLField;
    
    private string typeField;
    
    /// <remarks/>
    public string _comment {
        get {
            return this._commentField;
        }
        set {
            this._commentField = value;
        }
    }
    
    /// <remarks/>
    public string acronym {
        get {
            return this.acronymField;
        }
        set {
            this.acronymField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("expanded-acronym")]
    public string expandedacronym {
        get {
            return this.expandedacronymField;
        }
        set {
            this.expandedacronymField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("sub-class-of")]
    public mimeinfoMimetypeSubclassof[] subclassof {
        get {
            return this.subclassofField;
        }
        set {
            this.subclassofField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("generic-icon")]
    public mimeinfoMimetypeGenericicon[] genericicon {
        get {
            return this.genericiconField;
        }
        set {
            this.genericiconField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("glob")]
    public mimeinfoMimetypeGlob[] glob {
        get {
            return this.globField;
        }
        set {
            this.globField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("magic")]
    public mimeinfoMimetypeMagic[] magic {
        get {
            return this.magicField;
        }
        set {
            this.magicField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("alias")]
    public mimeinfoMimetypeAlias[] alias {
        get {
            return this.aliasField;
        }
        set {
            this.aliasField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("root-XML")]
    public mimeinfoMimetypeRootXML[] rootXML {
        get {
            return this.rootXMLField;
        }
        set {
            this.rootXMLField = value;
        }
    }
        
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string type {
        get {
            return this.typeField;
        }
        set {
            this.typeField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetypeSubclassof {
    
    private string typeField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string type {
        get {
            return this.typeField;
        }
        set {
            this.typeField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetypeGenericicon {
    
    private string nameField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string name {
        get {
            return this.nameField;
        }
        set {
            this.nameField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetypeGlob {
    
    private string patternField;
    
    private string weightField;
    
    private string casesensitiveField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string pattern {
        get {
            return this.patternField;
        }
        set {
            this.patternField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string weight {
        get {
            return this.weightField;
        }
        set {
            this.weightField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute("case-sensitive")]
    public string casesensitive {
        get {
            return this.casesensitiveField;
        }
        set {
            this.casesensitiveField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetypeMagic {
    
    private match[] matchField;
    
    private string priorityField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("match")]
    public match[] match {
        get {
            return this.matchField;
        }
        set {
            this.matchField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string priority {
        get {
            return this.priorityField;
        }
        set {
            this.priorityField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetypeAlias {
    
    private string typeField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string type {
        get {
            return this.typeField;
        }
        set {
            this.typeField = value;
        }
    }
}

/// <remarks/>
[System.CodeDom.Compiler.GeneratedCodeAttribute("xsd", "4.0.30319.33440")]
[System.SerializableAttribute()]
[System.Diagnostics.DebuggerStepThroughAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType=true, Namespace="http://www.freedesktop.org/standards/shared-mime-info")]
public partial class mimeinfoMimetypeRootXML {
    
    private string namespaceURIField;
    
    private string localNameField;
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string namespaceURI {
        get {
            return this.namespaceURIField;
        }
        set {
            this.namespaceURIField = value;
        }
    }
    
    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string localName {
        get {
            return this.localNameField;
        }
        set {
            this.localNameField = value;
        }
    }
}